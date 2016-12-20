def digit_sum(n):
    sum = 0
    while(n>0):
        a = n%10
        sum = sum + a
        n = n/10
    return sum

digit_sum(1234)