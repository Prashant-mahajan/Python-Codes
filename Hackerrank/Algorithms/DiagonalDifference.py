#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
first = second = 0
for i in range(n):
    first += a[i][i]
    second += a[n-1-i][i]
print(abs(first-second))

