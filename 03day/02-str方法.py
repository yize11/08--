class Teacher():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def teach(self):
        print('教书育人')
    def sleep(self):
        print('睡觉')
    def eat(self):
        print('吃饭')
    def introduce(self):
        print('我叫%s,年龄%d'%(self.name,self.age))
    def __str__(self):
        msg = '我叫%s年龄%d'%(self.name,self.age)
        return msg
sy = Teacher('孙院',30)
sy.teach()
sy.sleep()
sy.eat()
