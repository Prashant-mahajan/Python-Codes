def factorial(x):
    fact = 1
    i = 1
    for i in range(x):
        fact += fact * i
    return fact