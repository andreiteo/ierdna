#!/usr/local/bin/python3
import sys
print(sys.version)

def max_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# == inseamna egal   ;    !# inseamna nu e egal cu
print(max_num(300, 4, 5))
