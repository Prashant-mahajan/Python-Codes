# Problem: https://www.hackerrank.com/challenges/sherlock-and-array/problem

#!/bin/python3

import sys

def solve(a):
    lsum = 0
    total = sum(a)
    for i in range(len(a)):
        total = total - a[i]
        if lsum == total:
            return('YES')
        lsum = lsum + a[i]
    return('NO')

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)