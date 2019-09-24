import json
from flask import Flask
from flask import request,make_response

app = Flask(__name__)
users_dict = {}

@app.route('/api/users/<int:uid>',methods=['POST'])
def create_user(uid):
    user = request.get_json()
    if uid not in users_dict:
        result = {
            'success': True,
            'msg': "user created successfully."
        }
        status_code = 201
        users_dict[uid] = user
    else:
        result = {
            'success': False,
            'msg': "user already existed."
        }
        status_code = 500
    respense = make_response(json.dumps(result),status_code)
    respense.headers["Content-Type"] = "application/json"
    return respense

@app.route('/api/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    user = users_dict.get(uid,{})
    if user:
        user = request.get_json()
        success = True
        status_code = 200
    else:
        success = False
        status_code = 404
    result = {
        'success': success,
        'data': user
    }
    response = make_response(json.dumps(result),status_code)
    response.headers['Content-Type'] = 'application/json'
    return response

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', debug=True, port=5000)