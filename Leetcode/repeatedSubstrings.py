class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # The string B would be substring of A only when there length is equal or len + 1
        n = math.ceil(len(B)/len(A))
        if B in A*n:
            return n
        
        if B in A*(n+1):
            return n + 1
        
        return -1
        
        
    
            
                    