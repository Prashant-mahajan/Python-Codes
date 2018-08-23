# Problem : https://www.hackerrank.com/challenges/equality-in-a-array/problem

#!/bin/python3

def equalizeArray(arr):
    #print(Counter(arr))
    d = dict((x,arr.count(x)) for x in set(arr))
    key, value = max(d.items(), key = lambda p: p[1])
    print(len(arr)-value)

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = equalizeArray(arr)

