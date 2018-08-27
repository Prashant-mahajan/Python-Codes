# Problem: https://www.hackerrank.com/challenges/service-lane/problem

#!/bin/python3

def serviceLane(cases, width):
    for i in range(len(cases)):
        a, b = cases[i][0], cases[i][1]
        select = width[a:b+1]
        print(min(select))

n, t = map(int, input().split())
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))
result = serviceLane(cases,width)


