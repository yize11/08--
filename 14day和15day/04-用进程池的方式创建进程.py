from multiprocessing import Pool
from time import sleep
def work(arg):
    for i in range(5):
        print('老王',arg)
        sleep(1)
p = Pool()#能装3个进程
for i in range(5):
    p.apply_async(work,(i,))#非阻塞添加
    #p.apply(work,(i,))#阻塞添加
    print('加入成功')
p.close()
p.join()
#p.terminate()
print('哈哈')
