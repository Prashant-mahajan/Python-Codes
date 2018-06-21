# Problem: https://www.hackerrank.com/challenges/quicksort1/problem

def quickSort(arr):   
    left, right, mid = [], [], []
    for i in range(len(arr)): 
        if arr[i] < arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            right.append(arr[i])
        else:
            mid.append(arr[i])
    print(*(left + mid+ right))


n = int(input())
arr = list(map(int, input().rstrip().split()))
result = quickSort(arr)

