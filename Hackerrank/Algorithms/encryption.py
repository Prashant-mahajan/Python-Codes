# Problem: https://www.hackerrank.com/challenges/encryption/problem

#!/bin/python3

import math
def encryption(s):
    s.replace(' ', '')
    l = len(s)
    row , col = math.floor(math.sqrt(l)), math.ceil(math.sqrt(l))
    if row*col < l:
        row , col = col, col
    for i in range(col):
        print(s[i::col], end = ' ')

s = input()
result = encryption(s)

