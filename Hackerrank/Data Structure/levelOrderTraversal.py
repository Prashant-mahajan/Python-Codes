"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
	#Write code Here
    h = height(root)
    for d in range(1, h+1):
        givenLevel(root, d)

def givenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data) ,
    elif level > 1:
        givenLevel(root.left, level - 1)
        givenLevel(root.right, level - 1)
        
def height(root):
    if root is None:
        return 0
    else:
        right = height(root.right)
        left = height(root.left)
    return max(right, left) + 1

