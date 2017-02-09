# -*- coding:utf-8 -*-
'''
Created on 2017年2月9日
@author: xiang
'''
# list

num_list = [1, 2, 45, 7, 4]
print("nember_list: " + str(num_list))  # 需要str()转换类型

string_list = ["abc", "bbc", "python"]

mixed_list = ["python", "java", 3, 12]

print("mixed_list: " + str(mixed_list))
print(mixed_list)
print("{0}  {1}  {2}").format(num_list[0], string_list[0], mixed_list[0])

print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
a = [1, 2, 3] + [4, 5, 6]
print(a)  # [1, 2, 3, 4, 5, 6]
print(["hello"] * 4)  # ['hello', 'hello', 'hello', 'hello']
print(3 in [1, 2, 3])  # True

# splice
abcd_list = ['a', 'b', 'c', 'd']
print(abcd_list[1])
print(abcd_list[:])
print(abcd_list[1:])  # ['b', 'c', 'd']
print(abcd_list[-2])  # c
print(abcd_list[-1])

print(type(abcd_list[:]))  # <type 'list'>
print(type(abcd_list[1]))  # <type 'str'>

a = list.pop(abcd_list)
print(a)
print(abcd_list)

a = list.sort(num_list)
print(a)
# 列表操作包含以下函数:
# 1、cmp(list1, list2)：比较两个列表的元素 
# 2、len(list)：列表元素个数 
# 3、max(list)：返回列表元素最大值 
# 4、min(list)：返回列表元素最小值 
# 5、list(seq)：将元组转换为列表 
# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
# 2、list.count(obj)：统计某个元素在列表中出现的次数
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
# 5、list.insert(index, obj)：将对象插入列表
# 6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7、list.remove(obj)：移除列表中某个值的第一个匹配项
# 8、list.reverse()：反向列表中元素
# 9、list.sort([func])：对原列表进行排序

# tuple
a = (1, 2, 3)
# a[0] = 11    TypeError: 'tuple' object does not support item assignment
print(a)
# del a[0]   error
# del a     right
print(len(a))
print((1, 2, 3) + (4, 5, 6))
print(("hello") * 4)
print(3 in (1, 2, 3))

# tuple slice
abcd_tuple = ('a', 'b', 'c', 'd')
print(abcd_tuple[1])
print(abcd_tuple[1:])
print(abcd_tuple[-2])
print(abcd_tuple[-1])

# tuple strange style
a = (2,)
mixed_tuple = (1, 2, ['a', 'b'])  # Can we change this tuple?
mixed_tuple[2][0] = 'c'
mixed_tuple[2][1] = 'd'
print(mixed_tuple)  # tuple is "changed" to (1, 2, ['c', 'd'])

v = ('a', 'b', 'c')
(x, y, z) = v
print(x, y, z)  # ('a', 'b', 'c')
vv = x, y
print(vv)  # ('a', 'b')
print(list(vv))  # ['a', 'b']
print(tuple(list(vv)))  # ('a', 'b')

# list []                   tuple()
# updatable         un-update
# slow                    fast
# tuple(list)           list(tuple)        change freely
