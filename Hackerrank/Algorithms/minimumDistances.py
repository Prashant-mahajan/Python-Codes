# Problem: https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

def minimumDistances(a):
    dif = len(a)
    d = {}
    for i in range(len(a)):
        try:
            dif = min(i-d[a[i]], dif)
            d[a[i]] = i
            if dif == 1:
                break
        except:
            d[a[i]] = i
    
    if dif == len(a):
        print(-1)
    else: 
        print(dif)

n = int(input())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)


