# Problem: https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

def pickingNumbers(a):
    max = 0 
    for i in range(len(a)):
        pos = neg = 0
        for j in range(len(a)):
            if (a[i] - a[j]) >= 0 and (a[i] - a[j]) <= 1:
                pos += 1
            if (a[i] - a[j]) <= 0 and (a[i] - a[j]) >= -1:
                neg += 1
        if max < pos:
            max = pos
        if max < neg:
            max = neg
    print(max)

    
n = int(input())
a = list(map(int, input().rstrip().split()))
result = pickingNumbers(a)

