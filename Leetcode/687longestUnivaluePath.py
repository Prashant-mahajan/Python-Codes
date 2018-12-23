# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.answer = 0
        self.maxDepth(root)
        return self.answer
        
    def maxDepth(self, node):
        if node is None: 
            return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        
        left = left + 1 if node.left and node.left.val == node.val else 0 
        right = right + 1 if node.right and node.right.val == node.val else 0
        
        # Keeps track of longest path visited so far
        self.answer = max(self.answer, left+right)
        
        return max(left,right) 