# Problem: https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

def getMoneySpent(keyboards, drives, b):
    amount = -1
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b and keyboards[i] + drives[j] > amount:
                amount = keyboards[i] + drives[j]
    print(amount)
    


bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)