
def get_functions(FUNCTIONS:list):
    functions_desc = ''
    function_template = '''
    {num}. **{function_name}**:
    \t- Description: {function_desc}'''

    required_arg_template = '''
    \t- **Required Arguments**:'''

    optional_arg_template = '''
    \t- **Optional Arguments**:'''

    no_arg_template = '''
    \t- **No arguments**.'''

    arg_item_template = '''
    \t\t- `{name}` ({type})'''

    num = 1
    for function in FUNCTIONS:
        desc = function_template.format(num=num, function_name=function['function']['name'], function_desc=function['function']['description'])
        if function['function']['parameters']['properties'] == {}:
            desc += no_arg_template
        else:
            try:
                req_fields = function['function']['parameters']['required']
                desc += required_arg_template
                args = function['function']['parameters']['properties']
                for req_field in req_fields:
                    arg = args[req_field]
                    if arg['type'] == 'array':
                        item_type = arg["items"]["type"]
                        arg_type = f'array of {item_type}s'
                    else:
                        arg_type = arg['items']['type']
                    desc += arg_item_template.format(name=req_field, type=arg_type)
                # optional 있는 경우 추가
                diff_set = set(args.keys()) - set(req_fields)
                if len(diff_set) > 0:
                    desc += optional_arg_template
                    for key in list(diff_set):
                        arg = args[key]
                        if arg['type'] == 'array':
                            item_type = arg["items"]["type"]
                            arg_type = f'array of {item_type}s'
                        else:
                            arg_type = arg['type']
                        desc += arg_item_template.format(name=key, type=arg_type)
            except:
                desc += optional_arg_template
                args = function['function']['parameters']['properties']
                for key in args.keys():
                    arg = args[key]
                    if arg['type'] == 'array':
                        item_type = arg["items"]["type"]
                        arg_type = f'array of {item_type}s'
                    else:
                        arg_type = arg['type']
                    desc += arg_item_template.format(name=key, type=arg_type)
        functions_desc += desc
        num += 1

    return functions_desc

def get_shared_args(shared_arguments:dict):
    args_desc = ''
    arg_obj_template = '''
    {num}. **{arg_name}** (object):
    \t- Description: {arg_desc}
    \t- Keys:'''

    arg_obj_key_default_template = '''
    \t\t- {name} ({type}, default: {default}) - {key_desc}'''

    arg_obj_key_template = '''
    \t\t- {name} ({type}) - {key_desc}'''

    arg_simple_template = '''
    {num}. **{arg_name}** ({type}):
    \t- Description: {arg_desc}'''
    num = 1
    for arg_name in shared_arguments:
        content = shared_arguments[arg_name]
        if content['type'] == 'object':
            arg = arg_obj_template.format(num=num, arg_name=arg_name, arg_desc=content['description'])
            keys = content['properties']
            for key in keys:
                item = keys[key]
                try:
                    default_val = item['default']
                    arg += arg_obj_key_default_template.format(name=key, type=item['type'], key_desc=item['description'], default=default_val)
                except:
                    arg += arg_obj_key_template.format(name=key, type=item['type'], key_desc=item['description'])
        else:
            if content['type'] == 'array':
                item_type = content["items"]["type"]
                arg_type = f'array of {item_type}s'
            else:
                arg_type = content['type']
            arg = arg_simple_template.format(num=num, arg_name=arg_name, type=arg_type, arg_desc=content['description'])
        args_desc += arg
        num += 1
    return args_desc

def system_prompt_context(text:str):
    """You're a function classifier that needs to identify the appropriate function related to SKTelecom rate plans in order to accurately respond to the user's utterances.  You're actively involved in a three-way conversation with 'user', 'function' and yourself ('assistant').  You must classify the appropriate "function name" and "arguments" according to the user's utterance, and keep the following rules:
    1. "Function name" must be classified only from the lists provided below. You SHOULD NEVER GUESS and CREATE something that is not in the defined list.
    2. Arguments may or may not be required depending on the selected function.
    3. If the selected function has a 'required' field, you must fill in the arguments and send it.
    4. Arguments can be inferred from the user's utterance or the previous conversation."""
    return text


def get_system_prompt(plan_list=None, lineup_list=None, args_desc=None, functions_desc=None, examples=None, **kwargs)->str:

    # Initialize system prompt
    context = system_prompt_context.__doc__

    # generate system prompt
    system_prompt = f"{context}"

    if kwargs.get('plan_list') is True and plan_list is not None:
        system_prompt += f"\n\n### SKTelecom mobile plans\n{plan_list}"

    if kwargs.get('lineup_list') is True and lineup_list is not None:
        system_prompt += f"\n\n### SKTelecom mobile plan lineups\n{lineup_list}"

    system_prompt += f"\n\n### Shared Arguments\nThese argumentsd are shared by multiple functions.{args_desc}" if args_desc is not None else ''
    system_prompt += f"\n\n ### Function Descriptions:{functions_desc}" if functions_desc is not None else ''
    system_prompt += f"\n\n{examples}" if examples is not None else ''
    return system_prompt if len(context) != len(system_prompt) else None

if __name__=='__main__':

    sys_prompt = get_system_prompt()
    print(f'{sys_prompt = }')
