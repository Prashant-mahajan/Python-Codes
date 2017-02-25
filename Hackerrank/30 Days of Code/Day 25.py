import math

n = int(input().strip())
prime = 0
arr = [int(input()) for i in range(int(n))]

for x in arr:
    prime = 0
    a = int(math.sqrt(x))
    if a>1:
        for y in range(2,a+1):
            if x%y==0:
                prime +=1
                break
    if x == 1:
        print("Not prime")
    elif prime>0:
        print("Not prime")
    else:
        print("Prime")