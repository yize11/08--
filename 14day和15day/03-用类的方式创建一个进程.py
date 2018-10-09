from multiprocessing import Process
from time import sleep
class MyProcess(Process):
    def __init__(self):
        super().__init__()
    def run(self):
        for i in range(9):
            print('老王')
            sleep(1)
p = MyProcess()
p.start()
p.join()
print('哈哈')
