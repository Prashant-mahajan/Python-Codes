# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        
        if (p and not q) or (q and not p):
            return False
        
        if p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) :
                return True
            
        return False