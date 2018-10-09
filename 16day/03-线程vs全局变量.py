from threading import Thread
import time
num = 0
def test1(l):
    global num 
    time.sleep(1)
    num+=1
    l.append(44)
    print('test1',l)
    print('test1',num)
def test2(l):
    time.sleep(5)
    print('test2',l)
l1 = [11,22,33]
t1 = Thread(target=test1,args=(l1,))
t2 = Thread(target=test2,args=(l1,))
t1.start()
t2.start()
