#!/bin/python3

import os
import sys

#
# Complete the maximumProgramValue function below.
#
def maximumProgramValue(n):
    a = x = 0
    for i in range(n):
        user = input()
        if user[:3] =='add' and user[4] != '-': 
            x += int(user[4:])
        if user[:3] == 'set' and x < int(user[4:]): 
            x = int(user[4:])
    return(x)
            
                       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = maximumProgramValue(n)

    fptr.write(str(result) + '\n')

    fptr.close()