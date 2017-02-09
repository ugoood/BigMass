# -*- coding:utf-8 -*-
'''
Created on 2017年2月9日
@author: xiang
'''
# if    if elif     for
number = 59
# CAUSION int(input('Enter an integer : '))
# to wait user typing a number on console!
#guess = int(input('Enter an integer : '))       
#print('guess is : ' + str(guess))

# for loop

for i in range(1, 10):
    print(i)
else:
    print('The for loop is over.')

ran = range(1, 10)      #<type 'list'>
print(type(ran))

# not only list can do this, tuple & dict also can do that
a_list = [1, 3, 5, 7, 9]        #list
for i in a_list:
    print i

a_tuple = (1, 3, 5, 7, 9)       #tuple
for i in a_tuple:
    print i
else: print("loop over")

#CAUSION:  elem is a KEY !
a_dict = {'Tom' : 111, 'Jerry' : 222, 'Cathy' : 333}
for elem in a_dict:
    print(elem)         
    print(a_dict[elem])

#CAUSION:  dict.items()
for key, value in a_dict.items():
    print(type((key, value)))       # tuple
    print (key, value)