def closestNumbers(arr):
    arr.sort()
    ans = [arr[0], arr[1]]
    minDistance = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if (arr[i+1] - arr[i]) < minDistance: 
            ans = []
            minDistance = arr[i+1] - arr[i]
            ans.extend((arr[i], arr[i+1])) 
        elif arr[i+1] - arr[i] == minDistance:
            ans.extend((arr[i], arr[i+1])) 
    print(*ans)
       
n = int(input())
arr = list(map(int, input().rstrip().split()))
result = closestNumbers(arr)

