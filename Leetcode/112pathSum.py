# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        
        sum -= root.val 
        
        if not root.left and not root.right:
            return sum == 0
        
        return self.hasPathSum(root.right, sum) or self.hasPathSum(root.left, sum)


        # Iterative Version
        
        # if not root:
        #     return False

        # stack = [(root, sum-root.val)]
        # while stack:
        #     node, val = stack.pop()
            
        #     if not node.left and not node.right and val == 0:
        #         return True
            
        #     if node.right:
        #         stack.append((node.right, val-node.right.val))
            
        #     if node.left:
        #         stack.append((node.left, val-node.left.val))
        # return False
    