# Problem: https://www.hackerrank.com/challenges/library-fine/problem

#!/bin/python3

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return(10000)
    if y1 == y2:
        if m1 > m2:
            return(abs(m1-m2)*500)
        if m1 == m2 and d1 > d2:
            return(abs(d1-d2)*15)
    return(0) 

d1M1Y1 = input().split()
d1 = int(d1M1Y1[0])
m1 = int(d1M1Y1[1])
y1 = int(d1M1Y1[2])

d2M2Y2 = input().split()
d2 = int(d2M2Y2[0])
m2 = int(d2M2Y2[1])
y2 = int(d2M2Y2[2])
result = libraryFine(d1, m1, y1, d2, m2, y2)
print(result)

