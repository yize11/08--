import os
name = input('请输入文件夹的名字')
f = os.listdir(name)
print(os.getcwd())#查看路径
os.chdir(name)#切换路径
print(os.getcwd())#打印路径
for i in f:
    p = i.rfind('.')
    s = i[:p]
    e = i[p:]
    num = s +'精品'+e
    os.rename(i,num)#重命名
