'''
Created on 2017年2月8日

@author: xiang
'''
import os
import requests

#print(os.getcwd()) #当前模块的路径

r = requests.get("http://www.baidu.com")
print(r.url)
print(r.encoding)
print(r.text)