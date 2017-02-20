# -*- coding:utf-8 -*-
'''
Created on 2017年2月10日
@author: xiang
'''
# File IO
# 1. Write file
# 2. Read file
some_sentences = '''\
I love learning python
because python is fun
and also easy to use
床前明月光，
疑是地上霜，
举头望明月，
低头思故乡。
'''
# 1. Write a file
# Open for 'w'riting
f = open('sentences.txt', 'w')      # file is created on local workspace
# Write the text to File
f.write(some_sentences)
f.close()

# 2. Read a file
# CAUSION: if not specifying mode, 'r'ead mode is default
f = open("sentences.txt")
while True:
    #CAUSION: readline() return str(one line one str), but readlines() return a list
    #line = f.readlines()
    line = f.readline()
    print(type(line))
    # Zero length means End Of File, EOF
    if len(line) == 0:
        break
    print(line)
f.close     # CAUSION: f.close = f.close()