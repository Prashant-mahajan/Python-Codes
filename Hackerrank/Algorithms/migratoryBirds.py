# Problem: https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(ar):
    ans = [0]*6
    for i in range(len(ar)):
        ans[ar[i]] += 1
    print(ans.index(max(ans)))
            
ar_count = int(input()) 
ar = list(map(int, input().rstrip().split()))
result = migratoryBirds(ar)