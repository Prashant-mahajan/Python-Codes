#!/bin/python3
def findSuffix(strings, queryString):
    ans = 0
    for i in range(len(strings)):
        if strings[i] == queryString: 
            ans += 1
    print(ans) 

strings_count = int(input())
strings = []
for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

q = int(input())

for q_itr in range(q):
    queryString = input()
    findSuffix(strings, queryString)


# shorter version 

# s = [input() for _ in range(int(input()))]
# for _ in range(int(input())):
#     print(s.count(input()))