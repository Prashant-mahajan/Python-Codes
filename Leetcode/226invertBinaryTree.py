# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None 
        temp = root.left
        root.left = root.right
        root.right = temp 
        if root.right is not None: 
            self.invertTree(root.right)
        if root.left is not None: 
            self.invertTree(root.left)
        
        return root


        # Shorter version 
        if not root:
            return None
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root