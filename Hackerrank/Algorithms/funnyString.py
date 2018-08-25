# Problem: https://www.hackerrank.com/challenges/funny-string/problem

#!/bin/python3

def funnyString(s):
    dif = []
    for i in range(len(s)-1):
        dif.append(abs(ord(s[i])- ord(s[i+1])))
    print('Funny' if dif == list(reversed(dif)) else 'Not Funny' )
    
q = int(input())
for q_itr in range(q):
    s = input()
    result = funnyString(s)


