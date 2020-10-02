"""
协程的使用
yield , next()， send()
yield from  python 3.3引入
asyncio python 3.4 引入， 提供了事件循环的实现， 使得协程的高并发成为可能
async/wait 定义原生协程 原生协程要快于基于生成器的协程


"""

import asyncio


def gen():
    n = 0
    while True:
        yield n
        print(f'this n = {n}')
        n += 1


# 调用gen() 函数并不会直接执行该函数， 而是会得到一个生成器对象
g = gen()
print(g)
# 生成器对象调用next()， 这个生成器对象开始执行到第一个处， 于是产生一个值0， 这时候gen() 就暂停在yield处， 直到第二次调用next() 函数
# 每次执行到yield处将yield后方的值产出给调用方后就暂停自己的执行， 直到调用方下一次驱动它执行
print(next(g))
print(next(g))


def gen():
    s = yield "hello"
    print(f'user send value is {s}')
    yield s


# 得到一个生成器对象
g = gen()
# 得到字符串“hello" 后暂停执行， 得到打印输出
print(next(g))
# 通过调用send发送一个字符串给生成器函数， 这时候， 生成器函数将world 赋值给s, 继续它的执行， 直到第一个yield 处
print(g.send("world"))


# def func():
#     for x in 'ABC':
#         yield x


# 用于简化上面的for循环
def func():
    yield from 'ABC'


for x in func():
    print(x)


def func2():
    """生成器函数"""
    n = 0
    while True:
        s = yield n
        if s is None:
            break
        n += 1
    return n


def deligate():
    """委派生成器， 相当于添加一个代理了"""
    result = yield from func2()
    print(f'the result is {result}')


g = deligate()
print(next(g))
for i in range(3):
    print(g.send(i))

try:
    g.send(None)
except StopIteration:
    pass


# @asyncio.coroutine
# def get_html(url, name):
#     print(f'get {name}, html start {url}')
#     yield from asyncio.sleep(2)
#     print(f'get {name} html end {url}')


# 注意方法描述中添加关键字async, await 用法和yield from 类似
async def get_html(url, name):
    print(f'get {name}, html start {url}')
    await asyncio.sleep(2)
    print(f'get {name} html end {url}')


loop = asyncio.get_event_loop()
tasks = [
    get_html("http://www.baidu.com", "Baidu"),
    get_html("http://www.baidu.com", "Zhifu"),
]

loop.run_until_complete(asyncio.wait(tasks))

