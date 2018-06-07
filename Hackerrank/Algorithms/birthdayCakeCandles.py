# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem

#!/bin/python3

ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
a = max(ar)
count = 0
for i in range(len(ar)):
    if a == ar[i]:
        count += 1
print (count)