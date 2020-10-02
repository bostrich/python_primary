"""
元组：
元组与列表区别：元组可以存储多个数据， 元组内数据不能修改
常见操作：
    .index()
    .count()
    .len()
元组数据修改
    元组中的列表内中的数据可以修改
"""

# 定义元组, 使用方括号
num2 = [2, 5, "fd"]
nums = (1, 3, "df")
print(nums)
print(type(nums))
print(num2)
print(type(num2))

# 单个数据元组, 需要逗号， 如果不添加， 数据类型会改变
single = (10, )
single2 = (10)
print(type(single2))

