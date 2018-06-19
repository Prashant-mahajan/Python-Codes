# Problem: https://www.hackerrank.com/challenges/tutorial-intro/problem

#!/bin/python3
V = int(input())
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(arr.index(V))