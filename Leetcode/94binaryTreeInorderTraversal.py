# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        stack = []
        
        if not root: 
        	return ans

        while True:
        	if root is not None: 
        		stack.append(root)
        		root = root.left
        	else:
	        	if not stack:
	        		break
	        	root = stack.pop()
        		ans.append(root.val)
        		root = root.right
        return ans
        
        