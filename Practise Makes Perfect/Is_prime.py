def is_prime(x):
    if x==0 or x==1 or x < 0:
        return False
    for n in range(2,x-1):
        if x % n == 0:
            return False
    return True

