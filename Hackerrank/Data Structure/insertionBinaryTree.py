"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(root,val):
    if root is None:
        root = Node(val)
    else:
        if root.data > val:
            if root.left is None:
                root.left = Node(val)
            else:
                insert(root.left, val)
        else:
            if root.right is None:
                root.right = Node(val)
            else:
                insert(root.right, val)
    return root