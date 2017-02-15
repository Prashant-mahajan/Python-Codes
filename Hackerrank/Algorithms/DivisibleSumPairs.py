#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0
for i in range(n):
    for j in range(n):
        if ((i<j) and ((a[i]+a[j]) % k == 0)):
            count += 1
print(count)


