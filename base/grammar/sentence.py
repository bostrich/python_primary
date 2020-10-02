import random
"""
语句的使用
条件语句：if ... else ...
三目运算符：
循环
"""

# 条件成立，执行带缩进的代码行
if True:
    print("name")
    print("james")
else:
    print("koby")

# 多重判断 if ... elif ... else
# age = int(input('input age'))
age = random.randint(1, 50)
if age > 30:
    print(age)
elif age > 20:
    print(age)
else:
    print(age)


# 三目运算符 语法如下：条件成立执行的表达式 if 条件 else 条件不成立的表达式

'''
while 条件：
    代码1 
    代码2
    ...
    
    if i==4：
        break  终止循环，while...else中的代码不执行
    else：
        continue    终止本次循环， 进行下一次循环
        
else： while...else 当循环征程结束之后要执行的代码


for 临时变量 in 序列：
    代码1
    代码2
    
    
'''