#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    s = 0
    n = 0
    for i in range(len(rating)):
        if rating[i]>90:
            s += rating[i] 
            n = n + 1
    ans = (s/n) + 0.001
    print("{0:.2f}".format(ans))

if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)