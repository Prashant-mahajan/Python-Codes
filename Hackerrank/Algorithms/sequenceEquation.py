# Problem: https://www.hackerrank.com/challenges/permutation-equation/problem

n = int(input())
p = list(map(int, input().rstrip().split()))
for i in range(len(p)):
        print((p.index(p.index(i+1)+1))+1)


