import os
import time
pid = os.fork()
#子进程返回0
#父进程返回子进程的pid
print(pid)
if pid == 0:
    time.sleep(3)
    print('子进程%d,我的父亲是%d'%(os.getpid(),os.getppid()))
else:
    print('父进程%d'%os.getpid())
