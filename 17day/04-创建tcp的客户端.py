from socket import *
s = socket(AF_INET,SCOK_STREAM)

ip = input('请输入对方ip')
port = int(input('请输入对方端口'))
s.connect((ip,port))#三次握手
msg = input('请输入要发送的内容')
s.send(msg.encode('gb2312'))
while True:
    content = s.recv(1024)
    print(content.decode('gb2312'))

s.close()
