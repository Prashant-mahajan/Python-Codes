# Problem: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

# Node, Left, Right 
def preOrder(root):
    print(root.data) , # Prints values on the same line 
    if root.left is not None:
        preOrder(root.left)
    if root.right is not None: 
        preOrder(root.right)

# Left, Right, Node
def postOrder(root):
    #Write your code here
    if root.left is not None:
        postOrder(root.left)
    if root.right is not None:
        postOrder(root.right)
    print(root.data) , 

# Left, Node, Right
def inOrder(root):
    #Write your code here
    if root.left is not None:
        inOrder(root.left)
    print(root.data) ,
    if root.right is not None:
        inOrder(root.right)
