# -*- coding: utf-8 -*-
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
    def char2sum(c):
        return DIGITS[c]
    def char2float(c):
        return DIGITS[c]*0.1
    def f_integer(x,y):
        return x*10+y
    def f_decimal(x,y):
        return x*0.1+y

    index=s.find('.')
    s_inte=s[0:index]
    s_decm=s[index+1:]
    s_decm=s_decm[::-1]

    return reduce(f_integer,map(char2sum,s_inte))+reduce(f_decimal,map(char2float,s_decm))
    
str='123.4560434'
print(str2float(str))