import pandas as pd
from datetime import date
from tqdm import tqdm
import json
import requests
from utils import send_request_with_retry, save_pickle, compare_dicts, merge_keys_with_same_values
from set_logger import MyLogger
from collections import defaultdict

mylogger = MyLogger()

def run_and_evaluate(data:pd.DataFrame, **kwargs)->requests:
    """
    kwargs:
        skip_rows: int, number of rows to skip while quering againt LLM
        target_rows: set, index list to query. when this arg is implemented, skip_rows gets inactivated
        today: datetime, to record when the function has been run
    """
    # retrieve arguments
    skip_rows = kwargs.get('skip_rows', None)
    target_rows = kwargs.get('target_rows', None)
    today = kwargs.get('today', date.today())
    run_eval = kwargs.get('run_evaluate', True)

    assert not (skip_rows is not None and target_rows is not None), "skip_rows and target_rows are mutually exclusive"

    content_filter_file_name = kwargs.get('content_filter_file_name', f'content_filtered_{today}.pkl')
    false_index_file_name = kwargs.get('false_index_file_name', f'false_index_{today}.pkl')
    time_lapse_file_name = kwargs.get('time_lapse_file_name', f'time_lapse_{today}.pkl')

    # Initialize loop results
    false_index_list = {}
    time_lapse = {}
    content_filtered = {}
    original_response = {}

    # Iterate over the rows with progress bar
    pbar = tqdm(data.itertuples(), total=len(data))
    for row in pbar:
        row_id:str = str(row.Index)
        pbar.set_description(f'{row_id = }')

        if target_rows:
            if row_id not in target_rows:
                continue
        
        if skip_rows and int(row_id) < skip_rows:
            continue
        
        # update kwargs
        kwargs['user_query'] = row.Utterance_Sentence.strip()        
        
        # Measure the time while requesting
        try:
            response = send_request_with_retry(**kwargs)
            original_response[row_id] = response['original_response']
            res = response['content']
        except SystemExit:
            continue  # Skip this row if retries failed

        # Record time lapse for each user query
        try:
            time_lapse[row_id] = response['time_lapse']
            save_pickle(time_lapse, time_lapse_file_name, 'result')
        except KeyError as e:
            raise Exception(e)

        if res.get('content_filter'):
            content_filtered[row_id] = {}
            content_filtered[row_id]['filtered'] =  [policy for policy, filter_result in res['innererror']['content_filter_result'].items() if filter_result['filtered']]
            content_filtered[row_id]['user_query'] = kwargs['user_query']
            save_pickle(content_filtered, content_filter_file_name, 'result')
            continue

        # Compare response with true result
        if run_eval:
            true_result = json.loads(row.LLM_output)
            is_identical = compare_dicts(true_result, res)
            if not is_identical['result']:
                try:
                    false_index_list[row_id] = {}
                    false_index_list[row_id]['message'] = is_identical['message']
                    false_index_list[row_id]['user_query'] = kwargs['user_query']
                    save_pickle(false_index_list, false_index_file_name, 'result')
                except KeyError as e:
                    mylogger.error(f'error evaluating llm response: {is_identical}')
                    raise KeyError(e)
                
    return {'false_index_list':false_index_list, 'time_lapse': time_lapse, 'content_filter': content_filtered, 'original_response': original_response} 

# Function to convert the DataFrame into the desired JSON format
def categorize_and_convert(df):
    # Create a list to hold the categorized data
    categorized_data = {"lineup": []}
    
    # Dictionary to track lineups and products under them
    lineup_dict = {}

    # lineup similarity columns
    lineup_similarity_cols = [c for c in df.columns if '라인업' in c[:-1] 
                   and not '유사' in c[:-1] 
                   and not '요금제' in c[:-1]]
    mylogger.info(f'{lineup_similarity_cols = }')

    # plan similarity columns
    plan_similarity_cols = [c for c in df.columns if '요금제유사어' in c]
    mylogger.info(f'{plan_similarity_cols = }')

    for index, row in df.iterrows():
        # Extract the lineup and product name
        lineup_name = row['요금제 라인업, 혜택 라인업']
        product_name = row['상품명']

        # Combine all 라인업유사 fields into one list (ignoring empty values)
        lineup_similarities = [row[c] for c in lineup_similarity_cols]
        lineup_similarities = [str(item).strip() for item in lineup_similarities if item and item != 'None'] # Remove any empty strings from the list

        # Combine all 요금제유사 fields into on list (ignoring empty values)
        plan_similarities = [row[c] for c in plan_similarity_cols]
        plan_similarities = [str(item).strip() for item in plan_similarities if item and item != 'None'] # Remove any empty strings from the list

        # Prepare the dictionary for all product details
        product_details = {
            '상품ID': row['상품ID'],
            'template 카테고리': row['template 카테고리'],
            '월정액(VAT 제외)': row['월정액(VAT 제외)'],
            '세대': row['세대'],
            '유사어': list(set(plan_similarities)) if plan_similarities else None,
            '월정액(VAT 포함)': row['월정액(VAT포함)'],
            # '요금제_kw': row['요금제_kw']
        }
        
        # Check if the lineup already exists in the dictionary
        if lineup_name not in lineup_dict:
            # If it doesn't exist, create a new entry for the lineup
            lineup_dict[lineup_name] = {
                "name": lineup_name,
                'lineup_similarities': list(set(lineup_similarities)) if lineup_similarities else None,
                "products": []
            }
            categorized_data["lineup"].append(lineup_dict[lineup_name])
        
        # Append the product to the lineup
        lineup_dict[lineup_name]["products"].append({
            "product_name": product_name,
            "details": product_details
        })
    
    return categorized_data

# Function to create a prompt for ChatGPT
def create_lineup_prompt(data, **kwargs)->str:
    prompt = "### Below is a list of mobile lineups grouped by their respective similar words or phrases :\n"

    # Group lineups by '유사라인업'
    grouped_lineups = defaultdict(list)

    for lineup in data['lineup']:
        if lineup and lineup['lineup_similarities']:
            for similar in lineup['lineup_similarities']:
                if similar:
                    grouped_lineups[similar.strip()].append(lineup['name'])

    # merge keys with the same values
    grouped_lineups = merge_keys_with_same_values(grouped_lineups)

    cnt = 0
    for similar, lineups in grouped_lineups.items():
        if similar:
            cnt +=1
            prompt += f"{cnt}. **similarities:** {similar}\n"
            prompt += '  - **lineups:** ' + ', '.join(set([lineup.strip() for lineup in lineups if lineup and lineup is not None])) if lineups else ''
            prompt += '\n\n'

    # for lineup in data["lineup"]:
        # prompt += f"**Lineup: {lineup['name']}**\n"
        # prompt += f"  - **Lineup Similarities:** {lineup['lineup_similarities']}\n" if lineup['lineup_similarities'] else ''
        # prompt += f"  - **plans:** {', '.join([product['product_name'] for product in lineup['products']])}\n"
        # prompt += '\n'

    return prompt

def create_plans_prompt(data, **kwargs)->str:
    prompt = "### Below is a list of mobile plans grouped by their respective similar words or phrases. \n"
    
    # Group products by '유사어'
    grouped_products = defaultdict(list)

    for lineup in data["lineup"]:
        for product in lineup["products"]:
            similarities = product["details"]["유사어"]
            if similarities:
                for similar in similarities:
                    if similar:  # Only group if '유사어' is not None
                        grouped_products[similar.strip()].append(product["product_name"].strip())

    # merge keys with the same values
    grouped_products = merge_keys_with_same_values(grouped_products)

    # Generate Markdown prompt
    cnt = 0
    for similar, products in grouped_products.items():
        if similar:
            cnt += 1
            prompt += f"{cnt}. **similarities:** {similar}\n" 
            prompt += '  - **plans:** ' + ', '.join(set([product_name.strip() for product_name in products if product_name and product_name is not None])) if products else ''
            prompt +='\n\n'
        else:
            continue

    return prompt
