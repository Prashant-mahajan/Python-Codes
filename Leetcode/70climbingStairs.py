class Solution:
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [None]*(n)
        
        if n == 1:
            return 1 
        
        ans[0], ans[1] = 1, 2
        
        for i in range(2,n):
            ans[i] = ans[i-1] + ans[i-2]
            
        return ans[-1]
        
        