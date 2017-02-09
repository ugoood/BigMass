import sys

a = 3
b = 4

c = 5.66
d = 8.0

e = complex(c, d)
f = complex(float(a), float(b))

print("a is type: ", type(a))
print("c is type: ", type(c))
print("e is type: ", type(e))

print(b / a)  # 1.3333333333333333
print(b // a)  # 1

print(sys.float_info)  # sys包中float的最大最小值信息

'''字符串'''
print("hello")
print('hello')

# 打印多行
print('''first line
second line
third line''')

# Format字符串
age = 3
name = "Tom"
print("{0} was {1} years old.".format(name, age))
print(name + " was " + str(age) + " years old.")#注意str(),cast类型转换
print("What's your name?\nTom")





