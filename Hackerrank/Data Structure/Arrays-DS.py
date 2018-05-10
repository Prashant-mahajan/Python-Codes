#!/bin/python3

import os
import sys

#
# Complete the reverseArray function below.
#
def reverseArray(a):
    print(*a[::-1])


arr_count = int(input())

arr = list(map(int, input().rstrip().split()))

res = reverseArray(arr)