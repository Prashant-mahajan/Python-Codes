# Problem: https://www.hackerrank.com/challenges/find-the-median/problem

#!/bin/python3

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()
print(arr[int(len(arr)/2)])