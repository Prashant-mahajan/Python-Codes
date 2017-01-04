#!/bin/python3

import sys
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
a = b = c = 0
for i in arr:
    if i> 0:
        a += 1
    elif i < 0:
        b += 1
    else:
        c += 1
a = float(a)/len(arr)
b = float(b)/len(arr)
c = float(c)/len(arr)
print (str(a) + '\n' + str(b) + '\n' + str(c))



