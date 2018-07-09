# Problem: https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy
n, m = map(int, input().split())
ar = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(ar, axis=0)))

