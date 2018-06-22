# Problem: https://www.hackerrank.com/challenges/runningtime/problem

#!/bin/python3

def runningTime(arr):
    count = 0
    for i in range(len(arr)):
        j = i-1 
        key = arr[i]
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
            count += 1
        arr[j+1] = key
        # print(*arr)
    print(count)
    
n = int(input())
arr = list(map(int, input().rstrip().split()))
result = runningTime(arr)


