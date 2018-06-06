# Problem: https://www.hackerrank.com/challenges/qheap1/problem

from heapq import heappush, heappop
original = []
extra = []
n = int(input())

for _ in range(n):
    a = list(map(int, input().strip().split(' ')))  
    if a[0] == 1:
        heappush(original, a[1])
        
    elif a[0] == 2: 
        if original[0] == a[1]:
            heappop(original)
        else:
            heappush(extra, a[1])
            
    else:
        check = bool(extra)

        while check:
            if extra[0] == original[0]:
                heappop(extra) 
                heappop(original) 
                check = bool(extra)
            else:
                check = False
        print(original[0])