class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        
        # If difference in length is greater than 1, then it's false 
        if abs(len(s) - len(t)) > 1:
            return False
        
        if len(s) > len(t):
            # Avoids working on deletion logic
            return self.isOneEditDistance(t,s)
        
        for i in range(len(s)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    # Insertion
                    s = s[:i] + t[i] + s[i+1:]
                else:
                    # Replacement 
                    s = s[:i] + t[i] + s[i:]
                break 
        
        return s == t  or s == t[:-1]
            
    