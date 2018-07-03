#!/bin/python3

def maximumToys(prices, k):
    count = cost = 0 
    for i in range(len(prices)):
        if cost + prices[i] <= k:
            count += 1
            cost += prices[i]
        else: 
            break
    print(count)    

nk = input().split()
n = int(nk[0])
k = int(nk[1])
prices = list(map(int, input().rstrip().split()))
prices.sort()
result = maximumToys(prices, k)


