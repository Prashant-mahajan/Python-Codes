# Problem: https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

def countingValleys(n, s):
    count, down = 0, 0
    for i in range(len(s)):
        if s[i] == 'D':
            if count == 0:
                down += 1
            count -= 1
        if s[i] == 'U':
            count += 1
    print(down)


n = int(input())
s = input()
result = countingValleys(n, s)


