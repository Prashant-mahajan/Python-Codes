# Problem: https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    current = root
    output = []
    for i in range(len(s)):
        if s[i] == '0':
            current = current.left
        else: 
            current = current.right
        if (current.left is None and current.right is None):
            output.append(current.data)
            current = root
    print(''.join(output))

