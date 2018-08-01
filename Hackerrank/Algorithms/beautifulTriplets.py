# Problem: https://www.hackerrank.com/challenges/beautiful-triplets/problem

#!/bin/python3
    
n, d = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
count = 0
for i in range(n):
    if arr[i]+ d in arr and arr[i] + 2*d in arr:
        count += 1 
print(count)