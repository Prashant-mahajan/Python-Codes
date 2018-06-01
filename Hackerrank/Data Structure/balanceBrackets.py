# Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    arr = []
    for i in range(len(s)):
        if s[i] == '{' or s[i] == '[' or s[i] == '(':
            arr.append(s[i])
        elif s[i] == '}':
            if len(arr) == 0 or arr[-1] != '{':
                return 'NO'
            arr.pop()
        elif s[i] == ']':
            if len(arr) == 0 or arr[-1] != '[':
                return 'NO'
            arr.pop()
        elif s[i] == ')':
            if len(arr) == 0 or arr[-1] != '(':
                return 'NO'
            arr.pop()
        
    if len(arr) > 0:
        return 'NO'
    else:
        return 'YES'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

t = int(input())

for t_itr in range(t):
    s = input()

    result = isBalanced(s)

    fptr.write(result + '\n')

fptr.close()

