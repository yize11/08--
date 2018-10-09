from socket import *
#创建tcp的套接字
s=socket(AF_INET,SOCK_STREAM)
#绑定端口
s.bind(('',8080))
#监听过程
s.listen(5)
#等待连接
s1,add = s.accept()
#接受消息
msg = s1.recv(1024)
print(msg.decode('gb2312'))
#发消息
s1.send('哈哈'.encode('gb2312'))
s1.close()
s.close()
