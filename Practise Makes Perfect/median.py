def median(n):
    n = sorted(n)
    i = int(len(n)/2) 
    if len(n)%2 == 0:
        return (n[i] + n[i-1])/2.0
    else:
        return n[i]