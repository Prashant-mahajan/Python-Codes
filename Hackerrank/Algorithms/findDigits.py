# Problem: https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python3
for _ in range(int(input())):
    n = int(input())
    digits =[int(x) for x in str(n)] 
    count = 0
    for i in digits:
        if i !=0 and n%i == 0:
            count += 1
    print(count) 
   


