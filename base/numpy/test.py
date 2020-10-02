"""
numpy 使用
帮助处理数值型数据
快速， 方便， 便于后续科学计算基础库
存储数据类型：int8, unit8, int16, unit16,...
数组的形状： reshape函数， flatten()
广播：
索引和切片：

"""

# 文件名为numpy， 编译时报错
import numpy as np


ary1 = np.array([1, 3, 4])

ary2 = np.arange(10)
# 查看数据类型
print(ary2.dtype)
print(type(ary2))
print(ary2)

ary3 = np.array(range(0, 20, 5), dtype='float32')
print(ary3)
print(ary3.dtype)

print(ary3.shape)
ary4 = np.array([[1, 4, 5], [3, 5, 6]])
print(ary4)

ary4 = np.arange(12).reshape((3, 4))
print(ary4)


# ary[2:4, 1:4]
# ary[2:, 4:10]


