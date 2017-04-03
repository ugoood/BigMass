# -*- coding:utf-8 -*-
'''
Need: asking for Prime number
'''
import math
from time import time
import numpy as np

if __name__ == "__main__":
    def is_prime(x):
        return 0 not in [x % d for d in range(2, int(math.sqrt(x)) + 1)]


    a = 2
    b = 10000
    t = time()
    # 注意这句
    p = [p for p in range(a, b + 1) if 0 not in [p % d for d in range(a, int(math.sqrt(p)) + 1)]]
    print time() - t
    print p

    # Method 2: 利用filter
    t = time()
    p = filter(is_prime, range(a, b + 1))
    print time() - t
    print p

    # Method 3: 利用filter和lambda
