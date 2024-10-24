import pandas as pd
from datetime import date
from tqdm import tqdm
import json
import os
import requests
from utils import send_request_with_retry, save_pickle, compare_dicts
from set_logger import MyLogger

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
        
        true_result = json.loads(row.LLM_output)

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