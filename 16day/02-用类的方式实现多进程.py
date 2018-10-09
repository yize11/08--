from threading import Thread
import time
class MyThread(Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            print('哈哈'+self.name)
t1 = MyThread()
t2 = MyThread()
t1.start()
t2.start()
