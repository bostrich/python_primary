"""
http 访问 使用requests 模块


"""

import requests


def HttpGet(url):
    ret = requests.get(url)
    ret.encoding = 'utf-8'
    return ret.text


print(HttpGet("http://www.baidu.com"))
