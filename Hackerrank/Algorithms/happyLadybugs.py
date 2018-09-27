# Problem: https://www.hackerrank.com/challenges/happy-ladybugs/problem

#!/bin/python3
def happyLadybugs(b):
    for i in set(b):
        if i != "_" and b.count(i) == 1:
            return "NO"
    
    if b.count("_") == 0:
        for i in range(1,n-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                return "NO"
    return "YES"

g = int(input())
for g_itr in range(g):
    n = int(input())
    b = input()
    print(happyLadybugs(b))


