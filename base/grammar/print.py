
"""
格式化输出
常用格式化输出符号：
%s  字符串
%d  有符号的十进制整数
%f   浮点数
"""


# 格式化输出
name = "hello, 他们就不好了"
print('hello %s' % name)


# 控制浮点数显示的位数
weight = 62.3
print("体重 %.1f" % weight)

# 补全 %03d 位数补齐问题
num = 1
print('学号 %04d' % num)

print('学号 %03d, 体重 %.1f' % (num, weight))

