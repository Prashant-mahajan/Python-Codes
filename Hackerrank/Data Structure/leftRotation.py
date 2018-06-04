#!/bin/python3
n, d = map(int, input().strip().split())
a = [int(a_t) for a_t in input().strip().split()]
for i in range(d):
    a.append(a.pop(0))
print(*a)

