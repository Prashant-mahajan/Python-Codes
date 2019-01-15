class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {}
        start, end = 0, 0
        ans = 0
        
        while end < len(s):
            endchar = s[end]
            
            if endchar in table and table[endchar] >= start:
                start = table[endchar] + 1
                
            else:
                table[endchar] = end                             
                end += 1
        
            if end - start > ans:
                ans = end - start
        return ans