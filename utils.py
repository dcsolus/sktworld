import os
import time
import json
import requests
import pickle
from typing import Union, List, Dict, Set

# Payload for the request
def get_payload(system_prompt:str, user_prompt:str, temperature:float=0.0) -> dict:
    return {
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": system_prompt
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_prompt
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
        "temperature": temperature
    }

def send_request(system_prompt:str, user_prompt:str, **kwargs)->dict:
    ENDPOINT = f"{os.getenv('AZURE_OPENAI_ENDPOINT')}openai/deployments/{os.getenv('AZURE_OPENAI_MODEL_NAME')}/chat/completions?api-version={os.getenv('AZURE_OPENAI_API_VERSION')}"
    payload = get_payload(system_prompt, user_prompt)
    headers = kwargs.get('headers')

    # Send request
    try:
        start = time.time()
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        time_lapse = time.time() - start
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.HTTPError as e:
        if e.response.status_code == 400:
            # Handle 400 Bad Request error specifically
            error_detail = e.response.json() if e.response.content else "No additional error details"
            print(f"400 Client Error: {user_prompt = }")  # Print the error details
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
            result = json.loads(content)  # Load it as JSON

            # Inject time_lapse
            result['time_lapse'] = time_lapse
            return result
        else:
            raise ValueError("Unexpected response structure: 'choices' key not found or empty.")
            
    except ValueError as e:
        print(f"ValueError: {e}. Response content: {parsed_response}")
        raise SystemExit("Failed to parse the response as JSON.")
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}. Raw response: {response.text}")
        raise SystemExit("Failed to decode JSON response.")
    
def compare_dicts(dict1, dict2, path="")->dict:
    """Recursively compare two nested dictionaries, return True if they are identical, otherwise False.
    Also print the location of mismatches."""
    
    # Check if both are dictionaries
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        mismatch_info = f"Type mismatch at path '{path}': {type(dict1)} != {type(dict2)}"
        print(mismatch_info)
        return {'result': False, 'message':{'mismatch_info':mismatch_info, 'true_output': dict1, 'assistant_output': dict2}}

    # Compare the keys
    if dict1.keys() != dict2.keys():
        mismatch_info = f"Key mismatch at path '{path}': {dict1.keys()} != {dict2.keys()}"
        print(mismatch_info)
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
            mismatch_info = f"Value mismatch at path '{new_path}': {val1} != {val2}. type({type(val1)} != {type(val2)}), len({len(val1)} != {len(val2)})"
            print(mismatch_info)
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
    system_prompt = kwargs.get('system_prompt')
    headers = kwargs.get('headers')
    max_retries = kwargs.get('max_retries')
    wait_seconds = kwargs.get('wait_seconds')
    user_query = kwargs.get('user_query')
    
    # Define the error message
    error_message = f'Reactivating the requests after waiting for {wait_seconds} seconds...'
    retries = 0
    while retries < max_retries:
        try:
            return send_request(system_prompt=system_prompt, user_prompt=user_query, headers=headers)
        except SystemExit as e:
            retries += 1
            print(f"Attempt {retries} failed: {e}")
            
            # Since e is a SystemExit with a dictionary structure, we can access it directly
            error_details = e.args[0] if e.args else {}

            # Safely extract relevant keys from the error message
            error_message = error_details.get('error', {}).get('message', '')
            content_filter_code = error_details.get('error', {}).get('code', '')
            inner_error = error_details.get('error', {}).get('innererror', {})

            if content_filter_code == 'content_filter':
                return {
                    'content_filter': True, 
                    'innererror': inner_error
                }

            if retries < max_retries:
                print(error_message)
                time.sleep(wait_seconds)  # Wait before retrying
            else:
                print(f"Failed after {max_retries} attempts.")
                raise  # Re-raise the exception after all retries are exhaustedi