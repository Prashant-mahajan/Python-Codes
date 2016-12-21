N = int(input())
def Factorial(N):
    if N == 1:
        return 1
    else:
        return N * Factorial(N-1)

ans = Factorial(N)
print (ans)