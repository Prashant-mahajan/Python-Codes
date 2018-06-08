# Problem: https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3
from math import floor
x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])


if (v1> v2 and ((x2 - x1) % (v1-v2)) == 0): 
    print('YES')
else:
    print('NO')