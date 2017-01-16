input()
a = set(map(int, input().split()))
input()
b = set(map(int, input().split()))
ans = a.difference(b) 
ans.update(b.difference(a))
[print (i) for i in sorted(ans)]