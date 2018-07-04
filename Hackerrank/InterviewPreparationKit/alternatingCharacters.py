#!/bin/python3
def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    print(count)

q = int(input())
for q_itr in range(q):
    s = input()
    result = alternatingCharacters(s)

