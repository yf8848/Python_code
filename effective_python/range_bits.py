#!/bin/env python3

from random import randint

def range_bits():
    random_bits=0
    for i in range(64):
        if randint(0,1):
            random_bits |= i<<1
    return random_bits



if __name__ == "__main__":
    print("range bits num :",  bin(range_bits()) )
    