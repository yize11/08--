from multiprocessing import Pool,Manager
import time
def write(q):
    for i in range(10):
        time.sleep(0.5)
        q.put(i)
        print('写入成功')
def read(q):
    while True:
        num = q.get()
        print(num)
        if num == 9:
            break
p = Pool()
q = Manager().Queue()#创建队列
p.apply_async(write,(q,))
p.apply_async(read,(q,))
p.close()
p.join()
