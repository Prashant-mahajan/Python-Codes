def makeAnagram(a, b):
	for i in a:
		if i in b:
			a = a.replace(i, '', 1)		# Only one occurrence is replaced at a time 
			b = b.replace(i, '', 1)
	print(len(a) + len(b))

a = input()
b = input()
res = makeAnagram(a, b)