from collections import Counter
X = int(input())
shoes = Counter(map(int, input().split()))
N = int(input())
earned = 0

for i in range(N):
    size, prize = map(int, input().split())
    if size in shoes:
        if shoes[size] > 0:
            earned += prize
            shoes.update({size:-1})
            
print(earned)