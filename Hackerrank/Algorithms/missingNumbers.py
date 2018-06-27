# Problem: https://www.hackerrank.com/challenges/missing-numbers/problem

#!/bin/python3

def missingNumbers(arr, brr):
    adict, bdict = {}, {} 
    for i in range(len(arr)):
        if arr[i] in adict:
            adict[arr[i]] += 1
        else: 
            adict[arr[i]] = 1
            
    for i in range(len(brr)):
        if brr[i] in bdict:
            bdict[brr[i]] += 1
        else: 
            bdict[brr[i]] = 1
            
    for (k1,v1), (k2, v2) in zip(adict.items(), bdict.items()):
        if v1 != v2:
            print(k1, end= ' ')

n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split()))
result = missingNumbers(arr, brr)


