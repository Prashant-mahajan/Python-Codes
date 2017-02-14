#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a.sort()
j = 0
for i in range(len(a)):
    copy = a[j]
    a[:] = [x - copy for x in a]
    count = len(a)
    print(count)
    a[:] = (value for value in a if value != 0)
    #print(a)