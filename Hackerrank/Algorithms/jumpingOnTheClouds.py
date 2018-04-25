# Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3
n = int(input())
c = list(map(int, input().rstrip().split()))
count = -1
i = 0
while(i<n): 
    if i < n-2 and c[i+2] == 0: 
        i += 1 
    i += 1
    count += 1
print(count) 


