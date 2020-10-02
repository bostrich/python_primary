"""
字典：字典里面的数据已键值对的形式出现
创建字典
常见操作
"""


'''
字典特点：
    符号为大括号
    数据以键值对形式出现
    各个键值之间用逗号隔开
'''
dic = {'name': 'Tom', 'age': 15, 'gender': '男'}

'''
增：字典序列[key] = 值， 如果存在， 就覆盖
删：
    del 字典序列[key]
    clear() 清空字典
改：
    字典序列[key] = 值
查：
    根据key 直接查找： dic['name']
    字典序列.get(key, 默认值）
遍历：
    遍历字典key      for key in dic.keys()
    遍历字典value    for value in dic.values()
    遍历字典元素      for item in dic.items()
        
    
'''