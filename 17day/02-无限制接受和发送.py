#配置信息
#1、对方的ip
#2、对方端口
#创建一个udp套接字
from threading import Thread
import socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(('',8888))
ip = str(input('请输入对方ip地址'))
port = input('请输入对方端口')
def send():
    while True:
        print(ip,port)
        content = input('请输入发送消息')
        s.sendto(content.encode('gb2312'),(ip,port))
        print('呵呵')

def recv():
    while True:
        msg = s.recvfrom(1024)
        print(msg[0].decode('gb2312'))
t1 = Thread(target = send)
t2 = Thread(target = recv)
t1.start()
t2.start()
t1.join()
t2.join()
