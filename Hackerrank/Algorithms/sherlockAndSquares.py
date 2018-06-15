# Problem: https://www.hackerrank.com/challenges/sherlock-and-squares/problem

#!/bin/python3

from math import sqrt 
from math import floor
from math import ceil 

def squares(a, b):
    print(int(floor(sqrt(b)) - ceil(sqrt(a)) + 1))

q = int(input())
for q_itr in range(q):
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    result = squares(a, b)

