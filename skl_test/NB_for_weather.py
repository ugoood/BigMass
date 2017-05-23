# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import arff
from cStringIO import StringIO
import pandas as pd
from pandas import DataFrame, Series

content = '''
@relation weather

@attribute outlook {sunny, overcast, rainy}
@attribute temperature real
@attribute humidity real
@attribute windy {TRUE, FALSE}
@attribute play {yes, no}

@data
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,72,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no
'''

# 在 PyCharm 中，使用 Alt + 6 快捷键，可快速调出项目中的全部 TODO 注释；
# TODO(kl@gmail.com): Use a "*" here for string repetition.

# load the csv file as a numpy matrix
# 我的例子读的是 *.arff 文件
f = StringIO(content)
data, meta = arff.loadarff(f)
df = DataFrame(data,
               columns=['outlook', 'temperature',
                        'humidity', 'windy', 'play'],
               index=range(1, 15))


# df['outlook']
# print df.describe()
# print df['outlook'].count() 列非NA值数量
# min max 列的最大最小值
# argmin argmax 最大最小值的索引
# print df['outlook'].values 获取列值

# 获取一列 唯一值列表
def att_uniq_val(att_name):
    # if att_name 不是字符串，return -1
    a = df[att_name].value_counts().index
    return list(a)


# df['outlook'].values
# ['sunny' 'sunny' 'overcast' 'rainy' 'rainy' 'rainy' 'overcast' 'sunny'
# 'sunny' 'rainy' 'sunny' 'overcast' 'overcast' 'rainy']

# p(X) 某名词列元素的prob
# 输入：列名字符串
# 输出：带平滑的 dict, 包含了列所有元素的概率密度估计
# 输入样例： p_a("play")
# 输出样例： {'yes': 0.625, 'no': 0.375}

def p_y(att_name):
    # 列元素总数
    total_items = df[att_name].count()
    print "总数：", total_items

    cardinality = att_uniq_val(att_name)
    print "cardinality: ", cardinality

    # 一列 cardinality 中每个元素的个数，返回值为 np.array
    results = []
    for card_item in cardinality:
        # 一列中某元素个数
        count = 0
        count = float(count)
        for item in df[att_name].values:
            if item == card_item:
                count = count + 1
                # count = float(count)
        results.append(count)

    a = np.array(results) + 1.0
    b = total_items + cardinality.__len__()
    results = a / b

    # 创建结果字典
    dict = {}
    tup = zip(cardinality, results)
    for key, var in tup:
        dict[key] = var

    return dict  # {'yes': 0.625, 'no': 0.375}


# 判断是否为数字
# print isinstance(75.0, (int, float))

def isnumber(aString):
    aString_ = aString
    try:
        float(aString_)
        return True
    except:
        return False


# TODO(Xiang, ugoood@163.com): add Laplacian Smoothing for avoiding zero probability values.
# p(Y=y, X=x)的联合概率密度估计,已平滑
# 输入： y列名，x列名，y值，x值，列名均为字符串,y值是标签(名词), x值可以是 "名词" 或 数字
# 输入样例:
#   p_ab("play", "windy", "yes", "TRUE")
#   p_ab("play", "temperature", "yes", "70.1")

def p_xy(col_y, col_x, y, x):
    # X列的基元素
    x_cardinality = att_uniq_val(col_x)
    y_cardinality = att_uniq_val(col_y)  # Y列基元素

    # a 变成 DataFrame 方便使用join方法
    a = DataFrame(df[col_y])
    b = df[col_x]
    c = a.join(b)

    # 联合概率总行数
    total_items = c[col_x].count()
    print "total_items: ", total_items

    a = y  # "no"
    b = x  # "sunny"

    a_b_count = 0.0
    for index in c.index:

        a_ = "".join(c.ix[[index]][col_y].values)  # "play"

        if isnumber(b):
            b__ = float(b)
            b_ = c.ix[[index]][col_x].values[0]  # "outlook"

            if (a == a_) & (b__ == b_):
                a_b_count += 1
        else:
            b_ = "".join(c.ix[[index]][col_x].values)
            if (a == a_) & (b == b_):
                a_b_count += 1

    # Laplacian Smoothing
    p = a_b_count + 1.0
    q = total_items + 1.0 * y_cardinality.__len__() * x_cardinality.__len__()
    print u"p(%s = %s, %s = %s) = %f" % (col_y, y, col_x, x, p / q)
    return p / q


# p_xy("play", "windy", "yes", "TRUE")
# p_xy("play", "temperature", "yes", "70.111")

# p(x|y)
def p_x_given_y(col_y, col_x, y, x):
    result = p_xy(col_y, col_x, y, x) / p_y(col_y)[y]
    return result


print p_x_given_y("play", "windy", "yes", "FALSE")

# 0.355555555556 yes true
# 0.622222222222 yes false
# 0.0888888888889 yes falsea
print 0.622222222222+0.355555555556+0.0888888888889  # TODO Wrong results