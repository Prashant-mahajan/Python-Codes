#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice = (1 if a0>b0 else 0) + (1 if a1>b1 else 0) + (1 if a2>b2 else 0)
bob = (1 if a0<b0 else 0) + (1 if a1<b1 else 0) + (1 if a2<b2 else 0)
print (int(alice), int(bob))