T = int(input())
s = []
while(T>0):
    s = input()
    for i in range(len(s)):
        if i%2 == 0:
            print (s[i] , end="")
    print ( end=" ")
    for i in range(len(s)):
        if i%2 != 0:
            print (s[i] , end="")
    print(" ")

