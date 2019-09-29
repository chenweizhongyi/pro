from multiprocessing import Process
import time

from tests import api_server

def process():
    api_server_process = Process(
        target=api_server.app.run
    )
    api_server_process.run()
    time.sleep(0.2)
    return api_server_process

# if __name__ == '__main__':
#     process()