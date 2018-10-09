from multiprocessing import Pool
import time


print('叫朋友吃饭')
def test():
    for i in range(10):
        time.sleep(1)
        return '朋友忙完了叫你'
def getRet(msg):
    print(msg)




p = Pool(3)
p.apply_async(func=test,callback=getRet)
for i in range(1000):
    print('去打王者荣耀')
    time.sleep(1)
