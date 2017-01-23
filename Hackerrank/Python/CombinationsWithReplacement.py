from itertools import combinations_with_replacement
s , n = input().split()
# *[...] is to print ['a','b'] as a b 
# sep = '\n' to print each permutation on new line
print (*[''.join(i) for i in combinations_with_replacement(sorted(s), int(n))], sep = '\n')