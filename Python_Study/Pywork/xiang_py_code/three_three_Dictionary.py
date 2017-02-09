# -*- coding:utf-8 -*-
'''
Created on 2017年2月9日
@author: xiang
'''
# Dictionary
# key : value  
# Create a dictionary
phone_book = {'Tom' : 123, 'Jerry' : 456, 'Kim' : 789} # no any constrain for type
mixed_dict = {'Tom' : 'boy', 11 : 23.5 }
print("Tom has phone number: " + str(phone_book['Tom']))

# alter value of "Tom"
phone_book['Tom'] = 999
print("Tom has phone number: " + str(phone_book['Tom']))

# add a new term in dict
phone_book['Heath'] = 888
print(phone_book)

# delete an element in dict
del phone_book['Tom']
print(phone_book)

# clear a dict
phone_book.clear()
print(phone_book)       # {}

# del dict
del phone_book
# print(phone_book) dict is not exist

# must be unique in keys
rep_test = {'name' : 'aa', 'age' : 5, 'name' : 'dd'}
print(rep_test)     # no error, but unique key in dict

# key is unchangble, we can use string or tuple be as a key
# lsit_dict = {['name'] : 'John', 'Age' : 13}     # error
lsit_dict = {('name') : 'John', 'Age' : 13}     # is ok
print(lsit_dict)
