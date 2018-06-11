#!/bin/python3

# Complete the solve function below.
def solve(s, d, m):
    add = 0
    for i in range(len(s)-m+1):
        if sum(s[i: i+m]) == d:
            add+= 1
    print(add)

n = int(input())
s = list(map(int, input().rstrip().split()))
dm = input().split()
d = int(dm[0])
m = int(dm[1])
result = solve(s, d, m)


