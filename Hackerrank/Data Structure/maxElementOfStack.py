# Problem: https://www.hackerrank.com/challenges/maximum-element/problem

class Stack:
    def __init__(self):
        self.items = [0]
        self.maximum = [0]

    def isEmpty(self):
       return self.items == []

    def push(self, item):
        self.items.append(item)
        if self.maximum[-1] <= item:
            self.maximum.append(item)
            
    def pop(self):
        if self.items[-1] == self.maximum[-1]:
            self.maximum.pop()
        self.items.pop()


s = Stack()
for _ in range(int(input())):
    num = input().split()
    if num[0] == '1': 
        s.push(int(num[1]))
    elif num[0] == '2':
        s.pop()
    else: 
        print(s.maximum[-1])