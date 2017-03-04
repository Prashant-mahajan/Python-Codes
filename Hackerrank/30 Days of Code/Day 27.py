from random import randint 
T = 5
print(T)
while(T > 0):
    a = [-10,0,10]
    n = randint(3,200)
    k = randint(1,n)
    print(n , k)
    for i in range(n-3):
        a.append(randint(-1000,1000))
    print (' '.join(map(str, a)))
    del a[:]
    T -= 1
        