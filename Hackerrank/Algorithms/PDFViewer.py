#!/bin/python3

import sys
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
h = list(map(int, input().strip().split(' ')))
word = list(input().strip())
pair = {}
for j in range(len(alpha)):
    key = alpha[j]
    value = h[j]
    pair[key] = value
#print(pair)
#print(word)
values = []
for i in range(len(word)):
    values.append(pair[word[i]])
height = max(values)
area = height * len(word)
print(area)
    