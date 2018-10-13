# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        L, ans = [ ], [ ]
        
        if root: 
            L.append(root)

        while L:
            level = [ ]
            for _ in range(len(L)):
                temp = L.pop(0)
                level.append(temp.val)

                if temp.left:
                    L.append(temp.left)
                if temp.right:
                    L.append(temp.right)
            ans.append(level)
            
        return ans
        