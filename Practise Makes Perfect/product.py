def product(n): 
    ans = 1
    for i in range(len(n)):
        ans = ans * n[i]
    return ans