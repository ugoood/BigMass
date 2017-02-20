# -*- coding:utf-8 -*-
'''
Created on 2017年2月10日
@author: xiang
'''
# OO & decorator

# Python OO example
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print("I'm " + self.name)
        print("my grade is: " + str(self.grade))

    def improve(self, amount):
        self.grade += amount

jim = Student("jim", 86)
jim.introduce()

jim.improve(10)
jim.grade += 1000
jim.introduce()

tom = Student('tom', 18)
tom.introduce()

# CAUSION: decorator
