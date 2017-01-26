from itertools import permutations
s , n = input().split()
# *[...] is to print ['a','b'] as a b 
# sep = '\n' to print each permutation on new line
print (*[''.join(i) for i in permutations(sorted(s),int(n))], sep = '\n')

