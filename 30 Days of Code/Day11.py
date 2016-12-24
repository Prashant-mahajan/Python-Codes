#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
max_score = -sys.maxsize-1 #stores min value (this is essential for negative test cases)
for i in range(4):
    for j in range(4):
        tmp = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        max_score = max(max_score, tmp)
print(max_score)