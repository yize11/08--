from threading import Thread,Lock
import time
num = 0
def test1():
    global num
    m.acquire()#抢锁
    for i in range(1000000):
        num+=1
    m.release()#释放锁
    print('test1',num)

def test2():
    global num
    m.acquire()
    for i in range(1000000):
        num+=1
    m.release()
    print('test2',num)
m = Lock()
t1 = Thread(target=test1)
t2 = Thread(target=test2)
t1.start()
t2.start()
