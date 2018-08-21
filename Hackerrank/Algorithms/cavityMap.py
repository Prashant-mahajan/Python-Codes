# Problem: https://www.hackerrank.com/challenges/cavity-map/problem

#!/bin/python3
def cavityMap(grid,n):
    for i in range(1, n-1):
        for j in range(1, n-1):
            if (grid[i][j] > grid[i+1][j] and grid[i][j] >grid[i-1][j] and
                grid[i][j] >grid[i][j+1] and grid[i][j] > grid[i][j-1]):
                grid[i][j] = 'X'
                
    for i in range(n):
        print("".join(str(x) for x in grid[i]))


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))
result = cavityMap(grid,n)

