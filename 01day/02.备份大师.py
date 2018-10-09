name = input('请输入要备份的文件的名字')
f = open('8.txt','r')
content = f.read()
p = name.rfind('.')
s = name[ :p]
e = name[p: ]
namenum = s+'备份'+e
f=open(name,'r')
f1 = open(namenum,'w')
while True:
    content = f.read(1024)
    f1.write(content)
    if len(content) == 0:
        break
f.close()
f1.close()






