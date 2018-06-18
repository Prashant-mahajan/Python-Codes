# Problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#!/bin/python3
for _ in range(int(input())):
    x,y,z = map(int, input().split())
    if abs(z-x) > abs(z-y):
        print('Cat B')
    elif abs(z-x) < abs(z-y): 
        print('Cat A')
    else:
        print('Mouse C')
