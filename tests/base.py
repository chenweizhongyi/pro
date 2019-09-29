from multiprocessing import Process
import unittest
import time

from . import api_server

class ApiServerUnittest(unittest.TestCase):
    """
    设置可以在测试中使用的HTTP服务器的测试用例类
    """

    @classmethod
    def setUpClass(cls):
        cls.api_server_process = Process(
            target=api_server.app.run
        )
        cls.api_server_process.start()
        time.sleep(0.2)

    @classmethod
    def tearDownClass(cls):
        cls.api_server_process.terminate()
