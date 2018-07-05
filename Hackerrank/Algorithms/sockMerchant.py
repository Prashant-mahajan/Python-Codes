#!/bin/python3
n = int(input())
ar = list(map(int, input().rstrip().split()))
print(sum(ar.count(i) // 2 for i in set(ar)))



