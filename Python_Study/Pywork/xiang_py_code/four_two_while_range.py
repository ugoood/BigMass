# -*- coding:utf-8 -*-
'''
Created on 2017年2月9日
@author: xiang
'''
# while loop
count = 10
guess_flag = True

while guess_flag:
    count = count-1
    if count == 0:
        guess_flag = False
        print("while loop will be over !")
    print('Xiang is handsome!')

# in a loop:
# break: stop running the rest code in the loop, and jump out of loop
# continue: cancle current loop, jump into next loop.
# CAUSION:      pass: means  "do nothing !"
a_list = [0, 1, 2]
print("using continue: ")
for i in a_list:
    if not i:       #CAUSION:  0 is False,  1 is True,  also notice 'not'
        continue
    print(i)

print("using pass: ")
for i in a_list:
    if not i:       
        pass        #CAUSION:  pass means "do nothing !"
    print(i)
