
"""
数据类型
数值：int， float
布尔型：bool
字符串：str
列表：list
元祖：tuple
集合：set
字典：dict
"""

print("test")

'''
检测数据类型函数 type()

'''

print(type('1'))

b = True
print(type(b))


name = 'name'
age = 18.0
# 字符串 格式化 f'{变量名}' 较为高效
print(f'my name is {name}, age is {age + 1}')

'''
转义字符
\n  换行
\t  制表符， 一个tab键
'''
print('name', end="\t")
print('world')


