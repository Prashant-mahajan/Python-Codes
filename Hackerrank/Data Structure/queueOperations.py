# Problem: https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

from collections import deque

queue = deque([])

for _ in range(int(input())):
    num = input().split()
    if num[0] == '1': 
        queue.append(int(num[1]))
    elif num[0] == '2':
        queue.popleft()
    else: 
        print(queue[0])


