from itertools import product
A = map(int,input().split())
B = map(int,input().split())
C = [A, B]
print (' '.join(map(str,product(*C))))