#!/bin/python3

import sys

n = int(input().strip())
def fact(n):
    if n == 0:
        return (1)
    else:
        return n*fact(n-1)
print (fact(n))