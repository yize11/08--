class Cat():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('哈哈')
    def sleep(self):
        print('睡觉')
tom = Cat('tom',8)
tom.sleep()
print(tom.name)
print(tom.age)
