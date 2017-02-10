#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
array1 = [a,b,c,d,e]
array2 = [a,b,c,d,e]
ans1 = []
ans2 = []
sum1 = sum2 = 0
for i in range(4):
    ans1.append(max(array1))
    array1.remove(ans1[i])
    sum1 += ans1[i]
    #for min 
    ans2.append(min(array2))
    array2.remove(ans2[i])
    sum2 += ans2[i]
print (sum2,sum1)
    