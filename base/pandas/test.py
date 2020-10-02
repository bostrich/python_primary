"""
文档：
在numpy 基础上， 还可以处理字符串， 时间序列
series: 带标签的数组：
0    1
1    3
2    5
3    7
4    9
设置索引

dataFrame：二维数据


"""

import pandas as pd
import numpy as np


# pd.Series([1, 3, 5, 7, 9], index=list('abcde'))
se = pd.Series([1, 3, 5, 7, 9], index=list('abcde'))
print(se)

# 通过字典创建
dic = {"name": "james", "age": 18, "sex": "male"}
se2 = pd.Series(dic)
print(se2)

da = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(da)

