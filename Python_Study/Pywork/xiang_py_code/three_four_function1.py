# -*- coding:utf-8 -*-
'''
Created on 2017年2月9日
@author: xiang
'''
# function1
def say_hi():
    print('hi!')

say_hi()
say_hi()

# two peremeters
def print_sum_two(a, b):
    c = a + b
    # print(c)      has two peremeters, but still no any return value
    return c

print_sum_two(3, 5)
result = print_sum_two(3, 6)
print(result)

def repeat_str(str, times):
    repeated_strs = str * times
    return repeated_strs
stri = repeat_str("hi! ", 10)
print(stri)

# CAUSION: use term "global x" in a func to state a global variable in the func 
# Global variable  v.s.  Local variable
x = 60  # global vairable

def foo():
    global x
    #x = 4
    print(x)
    x = 3       # local variable
    print(x)

foo()
print(x)

