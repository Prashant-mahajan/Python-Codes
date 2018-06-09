# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

def breakingRecords(scores):
    minscore, maxscore = scores[0], scores[0]
    mincount, maxcount = 0, 0 
    for i in range(1, len(scores)):
        if scores[i] > maxscore:
            maxscore = scores[i]
            maxcount += 1
        if scores[i] < minscore:
            minscore = scores[i]
            mincount += 1
    print(maxcount, mincount)


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)

