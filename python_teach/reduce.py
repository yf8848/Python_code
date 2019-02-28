#!/bin/usr/env python3
from functools import reduce

def multi(x,y):
    return x*y

def prod(L):
    return reduce(multi,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))