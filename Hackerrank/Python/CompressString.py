from itertools import groupby
for i, c in groupby(input()):
    print((len(list(c)), int(i)), end =' ')
#The list is built of elements of (len(list(c)), int(i)).
#len(list(c)) = no.of occurences of a character c returned by the groupby function. 
#i = key value,the character itself.

