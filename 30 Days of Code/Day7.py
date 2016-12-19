#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
rev = []
j = int(len(arr))
for i in range(len(arr)):
    rev.append(arr[j-1])
    j -=1
    print(rev[i], end=" ") # , & end=" " are used to print all characters on same  line