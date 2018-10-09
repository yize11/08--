from socket import *
#创建一个udp的套接字
#AF_INET----IPV4
#SOCK_DGRAM-----UDP
s = socket(AF_INET,SOCK_DGRAM)
#s.sendto('你好'.encode('gb2312'),('192.168.43.126',8080))
while True:
    write = input('请输入你要发送的内容')
    s.sendto(write.encode('gb2312'),('192.168.43.126',8080))
    msg = s.recvfrom(1024)
    print(msg[0].decode('gb2312'),msg[1][0])
s.close()
