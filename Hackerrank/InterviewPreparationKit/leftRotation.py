#!/bin/python3
nd = input().split()
n = int(nd[0])
d = int(nd[1])
a = list(map(int, input().rstrip().split()))
print(*(a[d:] + a[:d]))

