#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    count = 1
    for i in range(n):
        if (i%2==0):
            count += count
        if(i%2 != 0):
            count += 1
    print(count)
    