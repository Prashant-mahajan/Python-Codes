D, M, Y = map(int ,input().split())
De, Me, Ye = map(int ,input().split())
if(Y - Ye > 0):
    print(10000)
elif(M == Me and Y == Ye):
    print(15* int(D - De))
elif((M-Me>0) and Y == Ye):
    print(500* int(M - Me))
else:
     print(0)

