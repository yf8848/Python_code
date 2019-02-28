#!/bin/usr/env python3

# -*- encoding: utf-8 -*-

def normalize(name):
    name = name.lower()
    return name[0:1].upper()+name[1:]

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)