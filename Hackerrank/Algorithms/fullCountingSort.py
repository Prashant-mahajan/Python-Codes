# Problem: https://www.hackerrank.com/challenges/countingsort4/problem

#!/bin/python3

n = int(input())
sort = {}
for i in range(n):
    xs = input().split()
    x = int(xs[0])
    s = xs[1]
    
    if i < n/2:
        s = '-'

    if x in sort:
        sort[x].append(s)
    else:
        sort[x] = [s]

for i in sort:
    print(*sort[i], end=' ')