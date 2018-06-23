# Problem: https://www.hackerrank.com/challenges/countingsort2/problem

#!/bin/python3

def countingSort(arr):
    results = [0]*100 
    for i in range(len(arr)):
        results[arr[i]] += 1
    # print(*results)
    for i in range(len(results)):
        while(results[i]):
            print(results.index(results[i]), end=' ')
            results[i] -= 1

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = countingSort(arr)



