from threading import Thread,current_thread
num = 0
def run():
    global num
    for i in range(10):
        num+=1
    print(current_thread().name,num)

def run1():
    global num 
    for i in range(10):
        num+=1
    print(current_thread().name,num)

t1 = Thread(target=run)
t2 = Thread(target=run1)


t1.start()
t2.start()

