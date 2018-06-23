# Problem: https://www.hackerrank.com/challenges/countingsort1/problem

#!/bin/python3

n = int(input())
arr = list(map(int, input().rstrip().split()))
results = [0]*100 
for i in range(len(arr)):
    results[arr[i]] += 1
print(*results)

