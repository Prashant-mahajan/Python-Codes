# Problem: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    if (root.data > v1 and root.data > v2):
        root = lca(root.left, v1, v2)
    if (root.data < v1 and root.data < v2):
        root = lca(root.right, v1, v2)
    else:
        return root

        