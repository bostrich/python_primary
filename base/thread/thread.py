"""
线程：
api 文档：https://docs.python.org/zh-cn/3/library/threading.html

协程：Coroutine

"""

import threading
import time

'''
创建新线程   threading.Thread(target=single())  需要导入模块 threading
 

'''


class MyThread(threading.Thread):

    # #
    # def __init__(self):
    #     print("myThread init")

    def run(self):
        print("myThread is running")


def single():
    num = 0
    while num < 5:
        print(f'single {num}')
        time.sleep(1)
        num += 1
        print(threading.current_thread().getName())


def dance():
    num = 0
    while num < 5:
        print(f'dance {num}')
        time.sleep(1)
        num += 1
        print(threading.current_thread().getName())


t1 = threading.Thread(target=single)
t2 = threading.Thread(target=dance, name='good')
t1.start()
t2.start()

# 自定义线程
t3 = MyThread()
t3.start()





