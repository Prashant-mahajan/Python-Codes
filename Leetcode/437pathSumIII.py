class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
    
    def findPath(self, root, sum):
        if root:
            return int(root.val == sum) + self.findPath(root.left, sum - root.val) + self.findPath(root.right, sum - root.val)
        return 0