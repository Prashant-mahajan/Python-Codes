class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        table = dict([i, p.count(i)] for i in p)
        left, right = 0, 0 
        counter = len(table)
        word = len(p)
        ans = []
        
        if len(s) < len(p) or len(s) == 0:
            return ans
        
        while right < len(s):
            endchar = s[right]
            
            if endchar in table:
                table[endchar] -= 1
                if table[endchar] == 0:
                    counter -= 1
            right += 1
            
            while counter == 0:
                if right - left == word:
                    ans.append(left)
                
                beginchar = s[left]
                
                if beginchar in table:
                    table[beginchar] += 1
                    if table[beginchar] > 0:
                        counter += 1
                left += 1
        return ans 
                        
        
# Shorter Method

from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        ans = []
        
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter: 
                ans.append(i-len(p)+1)
            
            sCounter[s[i-len(p)+1]] -= 1
            
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return ans