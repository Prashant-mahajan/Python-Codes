# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack , ans = [root], [ ]

        while stack:
            node = stack.pop()

            if node:
                ans.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return ans[::-1]
            