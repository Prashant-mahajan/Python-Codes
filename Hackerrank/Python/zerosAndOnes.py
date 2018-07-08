# Problem: https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy
ar = list(map(int, input().split()))
print(numpy.zeros(ar, dtype = numpy.int))
print(numpy.ones(ar, dtype = numpy.int))