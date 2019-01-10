# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        counter = 1
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if k is 0:
                    return root.val
                
                root = stack.pop()
                if counter is k:
                    return root.val
                counter += 1
                root = root.right 
        return None