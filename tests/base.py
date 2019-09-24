import multiprocessing
import time
import unittest
from . import api_server

class ApiServerUnittest(unittest.TestCase):
    """
    设置可以在测试中使用的HTTP服务器的测试用例类
    """
    @classmethod
    def setUpClass(cls):
        cls.api_server_process = multiprocessing.Process(
            target=api_server.app.run
        )
        cls.api_server_process.run()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.api_server_process.terminate()