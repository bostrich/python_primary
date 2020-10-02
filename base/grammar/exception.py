"""
异常
自定义异常
"""


class NotException(Exception):
    def __init__(self, length):
        self.length = length


def func():
    try:
        f = open('text.txt', 'r')
    except NameError:
        print("except")
    except IOError as result:
        print("none")
        print(result)
    except Exception as result:
        print(result)

    # 没有异常时执行
    else:
        print("normal end")
        # 抛出异常
        raise NotException(10)
    finally:
        print("end")


func()




