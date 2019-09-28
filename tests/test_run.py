import requests

def run_single_test_case(testcase):
    req_kwargs = testcase['request']

    try:
        url = req_kwargs.pop('url')
        method = req_kwargs.pop('method')
    except KeyError:
        raise ("Params Error")

    resp_obj = requests.request(url=url,method=method,**req_kwargs)
    diff = diff_response(resp_obj,testcase['response'])
    sucess = True if not diff else False
    return sucess,diff

def diff_response(resp_obj, expected_resp_json):
    diff_content = {}
    resp_info = parse_response_object(resp_obj)
    if resp_info['status_code'] not in expected_resp_json['status_code']:
        diff_content['status_code'] = resp_info['status_code']
    if resp_info['headers'] not in expected_resp_json['headers']:
        diff_content['headers'] = resp_info['headers']
    if resp_info['body'] not in expected_resp_json['body']:
        diff_content['body'] = resp_info['body']
    return diff_content

def parse_response_object(resp_obj):
    try:
        resp_resp = resp_obj.json()
    except Exception:
        resp_resp = resp_obj.text()
    return {
        'status_code': resp_resp.status_code,
        'headers': resp_resp.headrs,
        'body': resp_resp
    }
