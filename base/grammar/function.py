"""
函数
定义
调用
"""

'''
def 函数名（参数）：
    代码1
    代码2
    ...

注意事项：
    
    返回值： return  return 后的代码不执行
    
参数：
    位置参数：传递的参数与定义的顺序和个数需要一致
    关键字参数：函数调用， 通过“键=值” 的形式加以指定 user_info(gender = '男', age = 15)  关键字可以忽略顺序
    缺省参数: user_info(gender = '男')
    不定长参数： user_info(*args) 传递的参数会被合并成一个元组
    
'''


def func(s: str = "world"):
    """说明文档位置"""
    print(s)

    return "return"


print(func())
# 查看说明文档
print(help(func))
