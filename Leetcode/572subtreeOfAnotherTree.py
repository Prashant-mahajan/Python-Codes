class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if self.matched(s,t): 
            return True
        if not s: 
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) 
    
    def matched(self, s, t):
        if not (s and t):
            return s is t
        
        return s.val == t.val and self.matched(s.right, t.right) and self.matched(s.left, t.left)

        
            
        