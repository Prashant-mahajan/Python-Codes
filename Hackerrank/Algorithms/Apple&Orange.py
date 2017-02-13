#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
count1 = count2 = 0
for i in range(m):
    if (apple[i]+a >= s and apple[i]+a <=t):
        count1 += 1
for j in range(n):
    if (orange[j]+b <= t and orange[j]+b >= s):
        count2 += 1
print(str(count1) + '\n'+ str(count2))