from multiprocessing import Process
import time
num = 0
def test(a):
    global num
    for i in range(10):
        print('老王',a)
        num+=1
        time.sleep(1)
p = Process(target=test,args=('老宋',))#创建子进程
p.start()#子进程启动
#time.sleep(3)
#p.join()#让父进程等待子进程结束后在运行自己逻辑
p.join(3)#超时3秒
print(num)
print('哈哈哈')
