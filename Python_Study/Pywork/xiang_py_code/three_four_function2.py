# -*- coding:utf-8 -*-
'''
Created on 2017年2月9日
@author: xiang
'''
# function2
# default parameters
# VarArgs parameters  ----->  do not know the # of parameter in a func
# keyword parameters


# default params
def repeat_str(s, times = 1):
    repeated_strs = s * times
    return repeated_strs

print(repeat_str("he "))            #he
print(repeat_str("he ", 3))         #he he he 
print(repeat_str(5, 5))     #25

# f(a, b = 2) is right
# f(b = 2, a) is wrong

def func(a, b = 4, c = 8):
    print('a = ', a, 'b = ', b, 'c = ', c)

func(13, 17)    # ('a = ', 13, 'b = ', 17, 'c = ', 8)
func(125, c = 24)       #('a = ', 125, 'b = ', 4, 'c = ', 24)
#func(b = 40, 12)    # wrong
func(c = 40, a = 80)

# VarArgs paras and Keyword paras
# *nums is a tuple
# **words is a dictionary
def print_paras(fpara, *nums, **words):
    print("fpara: " + str(fpara))
    print("*nums: " + str(nums))
    print('**words: ' + str(words))

print_paras("hello", 1, 3, 5, 7, word = "python", another_word = 'java')

