class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 1
        self.maxDepth(root)
        return self.diameter - 1
        
    def maxDepth(self, root):
        if root == None:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)

        self.diameter = max(self.diameter, left + right + 1)
        return max(right, left) + 1 