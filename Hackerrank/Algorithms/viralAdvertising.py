# Problem: https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

from math import floor
cumulative, liked = 0, 0
shared = 5
for i in range(int(input())):
    liked = floor(shared/2)
    shared = liked * 3
    cumulative += liked 
print(cumulative)

