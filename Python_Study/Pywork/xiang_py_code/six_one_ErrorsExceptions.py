# -*- coding:utf-8 -*-
'''
Created on 2017年2月10日
@author: xiang
'''
# Error & Exceptions
'''
1. Syntax Errors    no need to explain
2. Exceptions
'''
# Handling exceptions
# while True:
#     try:
#         x = int(input("please enter a number"))
#         break
#     except ValueError:      # CAUSION: ValueError
#         print("Not valid input, man~")

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())      # CAUSION: strip() is to delete spaces in front of string 's'
except IOError as err:
    print("IO error: {0}".format(err))
except ValueError as ve:
    print("ValueError: {}".format(ve))
print(i)
