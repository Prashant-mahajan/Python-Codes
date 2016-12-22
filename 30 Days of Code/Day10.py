#!/bin/python3

import sys
n = int(input())
def Binary(n):
    convert = ("{0:b}".format(n))
    return convert
ans = max((Binary(n)).split('0')).count('1') #split removes O's from binary representation
print (ans)



#one line solution for this problem
#print(len(max(bin(n)[2:].split('0'))))

