# Problem: https://www.hackerrank.com/challenges/equal-stacks/problem

#!/bin/python3
n1N2N3 = input().split()
n1 = int(n1N2N3[0])
n2 = int(n1N2N3[1])
n3 = int(n1N2N3[2])

h1 = list(map(int, input().rstrip().split()))
h2 = list(map(int, input().rstrip().split()))
h3 = list(map(int, input().rstrip().split()))
a = sum(h1)
b = sum(h2)
c = sum(h3)

while(min(len(h1), len(h2), len(h3) != 0)):
    if a == b == c:
        print (a)
        break
    elif(a==max(a,b,c)):
        a = a - h1.pop(0)
    elif(b==max(a,b,c)):
        b = b - h2.pop(0)
    else:
        c = c - h3.pop(0)
        



