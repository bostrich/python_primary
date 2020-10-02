"""
列表的使用
列表可以存储多个数据， 而且可以是不同的数据类型
列表循环 while, for


"""

# 数据格式 使用中括号
names = ["james", "koby", "tolante", 12]
print(names[2])

'''
常用操作：
下标
.index(数据, 开始下标， 结束下标) 返回指定数据所在的下标
.count()
.len()
in 判断指定数据是否在某个数据列表中
.append()
.extend() 列表追加数据， 如果数据是一个序列， 则将这个序列的数据逐一添加到列表中
.insert(位置下标, 数据) 指定位置添加数据
del 
.pop()
.remove()
.clear()
.copy()

'''
print(names.index('james', 0, 6))
print(names.count("jaj"))
