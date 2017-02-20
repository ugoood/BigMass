# -*- coding:utf-8 -*-
'''
Created on 2017年2月11日
@author: xiang
'''
def power(x, n=2):    # n那就是默认参数
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(n=3, x=2))

def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())

# CAUSION: the *
def calc(*numbers):      
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

# def calc(numbers):
# print(calc([1,2,3]))        # list
# print(calc((1,2,3,4)))        # tuple

# def calc(*numbers):
print(calc(1,2,3))
print(calc(1,2,3,4))

nums = [11, 2, 3]
result=calc(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(result)

def person(name, age, **kw):
    print('name: ', name, '     age: ', age, '     other: ', kw)

person('Xiang', 37)     # name:  Xiang      age:  37      other:  {}
person('Bob', 30, city = 'Beijing', job = 'CS Engineer', gender = 'M')
# name:  Bob      age:  30      other:  {'gender': 'M', 'job': 'CS Engineer', 'city': 'Beijing'}

extra_info = {'gender': 'F', 'city': 'Chaihe'}
person('xiaoqiang', 22, city = extra_info['city'], gender = extra_info['gender'])
# name:  xiaoqiang      age:  22      other:  {'gender': 'F', 'city': 'Chaihe'}

person('xiaoqiang', 22, **extra_info)

def person(name, age, *, city, job):
    print(name, age, city, job)

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('Bob', 30, city = 'Beijing', job = 'CS_Engineer')

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))