import os
import math
import numpy as np
import codecs
import time
import json
import requests
import pickle
from typing import Union, List, Dict, Set
import pandas as pd
from set_logger import MyLogger

mylogger = MyLogger()

# Payload for the request
def get_payload(**kwargs) -> dict:
    return {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": kwargs.get('system_prompt')
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": kwargs.get('user_query')
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": ""
                    }
                ]
            }
        ],
        "temperature": kwargs.get('temperature', 0.0),
        "logprobs": True,
        # "top_p" : kwargs.get('top_p'),
    }

def send_request(**kwargs)->dict:

    user_query = kwargs.get('user_query')
    endpoint =  kwargs.get('endpoint')
    payload = get_payload(**kwargs)
    headers = kwargs.get('headers')

    # Send request
    try:
        start = time.time()
        response = requests.post(endpoint, headers=headers, json=payload)
        time_lapse = time.time() - start
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.HTTPError as e:
        if e.response.status_code == 400:
            # Handle 400 Bad Request error specifically
            error_detail = e.response.json() if e.response.content else "No additional error details"
            print(f"400 Client Error: {user_query = }")  # Print the error details
            raise SystemExit(error_detail) 
        else:
            # Handle other HTTP errors
            raise SystemExit(f"Failed to make the request. Error: {e}")

    try:
        parsed_response = response.json()

        # Ensure 'choices' is present and non-empty
        if 'choices' in parsed_response and parsed_response['choices']:
            # Extract the content that is a string representation of JSON
            content = parsed_response['choices'][0]['message']['content'].strip()

            # Remove the code block formatting (```json ... ```)
            if content.startswith("```json") and content.endswith("```"):
                content = content[7:-3].strip()  # Strip off the ```json and ```

            # Now load the cleaned content as JSON
            result = {}
            result['content'] = json.loads(content)  # Load it as JSON

            result['original_response'] = parsed_response

            # Inject time_lapse
            result['time_lapse'] = time_lapse
            return result
        else:
            raise ValueError("Unexpected response structure: 'choices' key not found or empty.")
            
    except ValueError as e:
        mylogger.error(f"ValueError: {e}. Response content: {parsed_response}")
        raise SystemExit("Failed to parse the response as JSON.")
    except json.JSONDecodeError as e:
        mylogger.error(f"JSONDecodeError: {e}. Raw response: {response.text}")
        raise SystemExit("Failed to decode JSON response.")
    
def compare_dicts(dict1, dict2, path="")->dict:
    """Recursively compare two nested dictionaries, return True if they are identical, otherwise False.
    Also print the location of mismatches."""
    
    # Check if both are dictionaries
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        mismatch_info = f"Type mismatch at path '{path}': {type(dict1)} != {type(dict2)}"
        mylogger.info(mismatch_info)
        return {'result': False, 'message':{'mismatch_info':mismatch_info, 'true_output': dict1, 'assistant_output': dict2}}

    # Compare the keys
    if dict1.keys() != dict2.keys():
        mismatch_info = f"Key mismatch at path '{path}': {dict1.keys()} != {dict2.keys()}"
        mylogger.info(mismatch_info)
        return {'result': False, 'message':{'mismatch_info':mismatch_info, 'true_output': dict1, 'assistant_output': dict2}}

    # Compare the values for each key
    for key in dict1:
        new_path = f"{path}->{key}" if path else key  # Build the path to the current key
        val1, val2 = dict1[key], dict2[key]

        # Check if both values are dictionaries (including empty ones)
        if isinstance(val1, dict) and isinstance(val2, dict):
            # Recursively compare nested dictionaries
            res = compare_dicts(val1, val2, new_path)
            if not res['result']:
                return {'result': False, 'message': res['message']}
        # Check for value mismatch and handle empty dictionaries
        elif val1 != val2:
            # Check if both are empty dictionaries or other empty types
            if isinstance(val1, dict) and isinstance(val2, dict) and not val1 and not val2:
                continue  # Both are empty dictionaries, consider them equal
            mismatch_info = f"Value mismatch at path '{new_path}': {val1} != {val2}. type({type(val1)} != {type(val2)})"
            mylogger.info(mismatch_info)
            return {'result': False, 'message':{'mismatch_info':mismatch_info, 'true_output': dict1, 'assistant_output': dict2}}

    return {'result':True, 'message':{}}

def save_pickle(content:Union[List, Set, Dict], file_name: str, result_dir:str) -> None:
    """Save content to a pickle file, handling different types and missing files."""

    assert isinstance(content, list) or isinstance(content, set) or isinstance(content, dict), "content should be list, set, or dict"
    
    # Check if file exists and load its content, otherwise initialize saved_content
    if os.path.exists(file_name):
        try:
            with open(file_name, 'rb') as f:
                saved_content = pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            # Handle empty file or unpickling errors (e.g., corrupted file)
            saved_content = None
    else:
        saved_content = None

    # Merge or process the content based on its type and existing saved_content
    if isinstance(saved_content, list):
        new_content = saved_content + content
    elif isinstance(saved_content, set):
        new_content = saved_content.intersection(content)
    elif isinstance(saved_content, dict):
        new_content = saved_content | content
    else:
        # Handle the case when there's no saved_content (e.g., first-time save)
        new_content = content

    # Save the updated content back to the pickle file
    file_path = os.path.join(result_dir, file_name)
    with open(file_path, 'wb') as f:
        pickle.dump(new_content, f)

def send_request_with_retry(**kwargs):
    """Send request and retry if a SystemExit is encountered.
    kwargs:
        system_prompt: str
        headers: str
        max_retries: int
        wait_seconds: int
        user_query: str
    """
    max_retries = kwargs.get('max_retries')
    wait_seconds = kwargs.get('wait_seconds')
    
    # Define the error message
    error_message = f'Reactivating the requests after waiting for {wait_seconds} seconds...'
    retries = 0
    while retries < max_retries:
        try:
            return send_request(**kwargs)
        except SystemExit as e:
            retries += 1
            mylogger.info(f"Attempt {retries} failed: {e}, kwargs: {kwargs.keys()}")
            
            # Since e is a SystemExit with a dictionary structure, we can access it directly
            error_details = e.args[0] if e.args else {'error': {'messages':None, 'code':None, 'innererror':None}}

            # Safely extract relevant keys from the error message
            error_message = error_details.get('error').get('messages', '')
            content_filter_code = error_details.get('error').get('code', '')
            inner_error = error_details.get('error').get('innererror', {})

            if content_filter_code == 'content_filter':
                return {
                    'content_filter': True, 
                    'innererror': inner_error
                }

            if retries < max_retries:
                mylogger.error(error_message)
                time.sleep(wait_seconds)  # Wait before retrying
            else:
                mylogger.error(f"Failed after {max_retries} attempts.")
                raise  # Re-raise the exception after all retries are exhaustedi

def get_aoai_endpoint_in4u()->str:
    return f"{os.getenv('AZURE_OPENAI_ENDPOINT')}openai/deployments/{os.getenv('AZURE_OPENAI_MODEL_NAME')}/chat/completions?api-version={os.getenv('AZURE_OPENAI_API_VERSION')}"


def parse_logprob(content)->dict:

    def is_ascii(char)->bool:
        return isinstance(char, str) and ord(char) < 128
    
    def get_none_ascii_key(keys:Union[List, Set])->list:
        # return values
        none_ascii_keys = [] 
        
        # decode key
        for key in keys:
            decoded_key = codecs.decode(key,'unicode_escape')
            res = [is_ascii(char) for char in decoded_key]
            if not all(res) and len(res) <= 2:
                none_ascii_keys.append(key)
        return none_ascii_keys
    
    threshold_index = [i for i, prob_dict in enumerate(content) if prob_dict['token']=='arguments'][0]
    logprob = {prob_dict['token'].strip():prob_dict['logprob'] for i, prob_dict in enumerate(content) 
                if i > threshold_index
                and len(prob_dict['token'].strip().strip(r'":[]{}.,').replace('keywords', '')) > 0}

    # remove none ascii keys 
    keys = list(logprob.keys())
    none_ascii_keys = get_none_ascii_key(keys)
    for k in none_ascii_keys:
        logprob.pop(k)

    # convert log value to probabilities
    probs = [math.exp(v) for v in logprob.values()]

    return {'logprobs':logprob, 'avg_prob': np.mean(probs)}


def logprob_main(df:pd.DataFrame, **kwargs):
    """
    Main function to process user query data and calculate log probabilities.

    This function cleans up the column names in the provided DataFrame, prepares a request
    to an external service(eg. Azure OpenAI), and retrieves log probabilities for each specified row of user
    queries. The results are returned as a dictionary indexed by the row indices.

    Parameters:
    ----------
    df : pd.DataFrame
        A DataFrame containing user query data, with a column named 'Utterance_Sentence'
        that holds the queries for which log probabilities are to be calculated.

    **kwargs : keyword arguments
        Additional parameters to be passed to the request, including:
        - data: The cleaned DataFrame.
        - system_prompt: A string that defines the system prompt for the request.
        - endpoint: The API endpoint for the external service.
        - temperature: A float controlling the randomness of the output (default is 0.0).
        - headers: A dictionary of HTTP headers to be included in the request.

    Returns:
    -------
    results : dict
        A dictionary where the keys are the indices of the DataFrame rows and the values
        are the calculated log probabilities for the corresponding user queries.

    Example:
    --------
    results = logprob_main(user_query_data)
    """

    from tqdm import tqdm

    # Clean up column names by replacing spaces with underscores
    df.columns = [c.replace(' ', '_') for c in df.columns]

    # define all the indices of the target rows, with which the iteration will be done
    target_rows = kwargs.get('target_rows', tuple())

    results = dict()
    pbar = tqdm(df.itertuples(), total=len(df))
    for row in pbar:
        pbar.set_description(f'{row.Index = }')
        if not str(row.Index) in target_rows:
            continue
        user_query = row.Utterance_Sentence
        kwargs['user_query'] = user_query
        response = send_request(**kwargs)
        content = response['original_response']['choices'][0]['logprobs']['content']
        logprob = parse_logprob(content)
        results[str(row.Index)] = logprob
    
    return results
