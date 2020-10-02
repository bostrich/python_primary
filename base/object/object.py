""""
面向对象

"""

'''
类的创建
class 类名（）：
    代码
    ...
    
注意： 类的命名使用大驼峰命名习惯

属性
对象的属性既可以在类外面添加和获取， 也能在类里面添加和获取

魔法方法：具有特殊功能的函数
__init_() 方法， 在创建一个对象时默认调用， 不需要手动调用
__str__
__del__

继承：

super(): 方法使用

私有属性和方法：不能够被继承
在属性和方法前面加上两个下划线__

类属性， 类方法
类属性， 只能通过类实现



'''


class Person(object):
    # 类属性
    name = "person"

    # 类方法
    @classmethod
    def age(cls):
        print('age is')

    # 静态方法 不需要参数传递， 有利于减少不必要的内存占用和性能消耗
    @staticmethod
    def live():
        print("live")

    # 初始化对象
    def __init__(self):
        # 添加实例属性
        name = "koby"

    # 带参数__init_()
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__money = 2000

    def get_money(self):
        return self.__money

    # 类似于Java toString() 方法
    def __str__(self):
        print("str")

    # 属性

    # self 指的是调用该函数的对象
    def writeLetter(self):
        print("write")
        print(f'width = {self.width}, height = {self.height}')


person = Person(10, 20)
# 类外面添加属性
person.name = "james"
print(person.name)
print(f'washer name is {person.name}')
print(person.get_money())


person.writeLetter()


'''
单继承：
多继承:

'''


class Student(Person):

    def __init__(self):
        print("student")
        super(20, 10)

    # 重写方法
    def writeLetter(self):
        print("new object")
        Person.writeLetter(self)
        # super 使用
        super().writeLetter()


# 多继承
class Junior(Student):
    def __init__(self):
        print("junior")


