from collections import Counter 
int(input())
a = input().split()
room = Counter(a)
print (min(room , key = room.get))

        
       