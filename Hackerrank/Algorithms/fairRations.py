# Problem: https://www.hackerrank.com/challenges/fair-rations/problem

#!/bin/python3

N = int(input())
B = list(map(int, input().rstrip().split()))
count = 0
if sum(B) % 2 != 0:
    print('NO')
else:
    for i in range(len(B)):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i+1] += 1
            count += 2
    print(count)

