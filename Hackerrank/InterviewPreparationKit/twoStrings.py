#!/bin/python3

def twoStrings(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] in s2 and count == 0:
            print('YES')
            count += 1
    if count == 0:
        print('NO')


q = int(input())
for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)

