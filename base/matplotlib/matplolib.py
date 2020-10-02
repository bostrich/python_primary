"""
python 绘图库， 数据可视化, 模仿matlab 构建



"""

# 导入 pyplot用于绘图

from matplotlib import pyplot as plt

# 设置图片大小
fig = plt.figure(figsize=(20, 8), dpi=80)


x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 25, 22, 18, 15]

#   设置X轴刻度
plt.xticks(range(2, 25))
plt.yticks(range(min(y), max(y) + 1))


plt.plot(x, y)

# 保存图片
# plt.savefig("./page.png")
# 保存svg 矢量图格式
# plt.savefig("./page.svg")

plt.show()

'''
设置图片大小
保存在本地

'''




