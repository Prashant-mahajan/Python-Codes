class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()
        size = len(S)
        first_group = K if size % K == 0 else size % K 
        
        ans = S[:first_group]
        while first_group < size:
            ans += '-' + S[first_group:first_group+K]
            first_group += K 
            
        return ans 

