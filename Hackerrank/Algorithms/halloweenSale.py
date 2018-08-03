# Problem: https://www.hackerrank.com/challenges/halloween-sale/problem

#!/bin/python3
def howManyGames(p, d, m, s):
    count = 0
    while(s>= 0):
        s -= p 
        p = max(p-d, m)
        count += 1
    print(count-1)

p, d, m, s = map(int,input().split())
answer = howManyGames(p, d, m, s)

