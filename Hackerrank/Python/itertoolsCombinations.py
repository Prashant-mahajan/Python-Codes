from itertools import combinations
s , n = input().split()
# *[...] is to print ['a','b'] as a b 
# sep = '\n' to print each permutation on new line
for i in range(1, int(n)+1):
    print (*[''.join(i) for i in combinations(sorted(s), i)], sep = '\n')


