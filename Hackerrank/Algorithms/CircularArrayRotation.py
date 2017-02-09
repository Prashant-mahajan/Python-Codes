#!/bin/python3

import sys
from collections import deque

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a = deque(a) 
a.rotate(k) #shift k places to right 
for a0 in range(q):
    m = int(input().strip())
    print(a[m])