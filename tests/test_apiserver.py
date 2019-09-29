import os

import requests
import time

from .base import ApiServerUnittest
from . import api_server
from . import test_run

class TestApiServer(ApiServerUnittest):

    def setUp(self):
        super(TestApiServer,self).setUp()
        self.host = 'http://127.0.0.1:5000'
        self.api_client =requests.Session()
        # self.clear_users()

    def tearDown(self):
        super(TestApiServer,self).tearDown()

    def test_create_user_not_existed(self):
        # self.clear_users()
        # url = "%s/api/users/%d" % (self.host,1000)
        # data = {
        #     "name": "user1",
        #     "password": "123456"
        # }
        # req = self.api_client.post(url,json=data)
        # self.assertEqual(201,req.status_code)
        # self.assertEqual(True,req.json()['success'])
        case_json = os.path.join(os.getcwd(),'tests/case/test.json')
        data = test_run.load_testcase(case_json)
        testcases = test_run.run_single_test_case(data)
        success = testcases[0]
        self.assertTrue(success)
