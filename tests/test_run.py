import requests
import json

def load_testcase(case_path):
    with open(case_path,'r') as f:
        data = json.load(f)
    return data

def run_single_test_case(testcase):
    req_kwargs = testcase['request']
    try:
        url = req_kwargs.pop('url')
        method = req_kwargs.pop('method')
    except KeyError:
        raise ("Params Error")

    resp_obj = requests.request(url=url,method=method,**req_kwargs)
    print('resp_obj_response:',resp_obj)
    diff = diff_response(resp_obj,testcase['response'])
    sucess = True if not diff else False
    return sucess,diff

def diff_response(resp_obj, expected_resp_json):
    # diff_content = {}
    resp_info = parse_response_object(resp_obj)
    print(type(resp_info),':resp_info:',resp_info)
    diff_content = diff_json(resp_info,expected_resp_json)
    return diff_content

def diff_json(current_json, expected_json):
    """
    比较实际结果与预期结果
    :param current_json:
    :param expected_json:
    :return:
    """
    json_diff = {}
    for key,expected_value in expected_json.items():
        value = current_json[key]
        if str(value) != str(expected_value):
            json_diff[key]={
                'value':value,
                'expected_value':expected_value
            }
    return json_diff

def parse_response_object(resp_obj):
    """
    将实际结果解析字典格式返回
    :param resp_obj:
    :return:
    """
    try:
        resp_resp = resp_obj.json()
    except Exception:
        resp_resp = resp_obj.text()

    print(type(resp_resp), ':resp_info:', resp_resp)
    return {
        'status_code': resp_resp.status_code,
        'headers': resp_resp.headrs,
        'body': resp_resp
    }
