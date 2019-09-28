import requests
import time

from .base import ApiServerUnittest
from . import api_server

class TestApiServer(ApiServerUnittest):

    def setUp(self):
        super(TestApiServer,self).setUp()
        self.host = 'http://127.0.0.1:5000'
        api_server.app.run()
        time.sleep(1)
        self.api_client =requests.Session()
        # self.clear_users()

    def tearDown(self):
        pass
        # super(TestApiServer,self).tearDown()

    def test_create_user_not_existed(self):
        # self.clear_users()
        url = "%s/api/users/%d" % (self.host,1000)
        data = {
            "name": "user1",
            "password": "123456"
        }
        req = self.api_client.post(url,json=data)
        self.assertEqual(201,req.status_code)
        self.assertEqual(True,req.json()['success'])