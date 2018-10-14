# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []
        values.append(root)
        ans = []
        
        if not root:
            return ans
                
        while(len(values) > 0):
            
            node = values.pop()
            ans.append(node.val)
            
            if node.right is not None:
                values.append(node.right)
                
            if node.left is not None:
                values.append(node.left)
                
        return ans
                

