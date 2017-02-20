# -*- coding:utf-8 -*-
'''
Created on 2017年2月10日
@author: xiang
'''
# IO Stream
# CAUSION:  input()   base on python version, 3.4version has no problem.
# str()     format

# Take input from user
str_1 = raw_input("Enter a string: ")
str_2 = str(input("Enter another string: ")

# Output the strings
print("str_1 is: " + str(str_1) + ". str_2 is: "  + str(str_2))
print("str_1 is {} str_2 is {}".format(str_1, str_2))
