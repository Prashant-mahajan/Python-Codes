class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        total = dict([i, t.count(i)] for i in t)
        start , end = 0, 0
        counter = len(total)
        ans = None
        length = sys.maxsize
        
        while end < len(s):
            endchar = s[end]
            
            if endchar in total:
                total[endchar] -= 1
                if total[endchar] == 0:
                    counter -= 1
            end += 1
            
            while counter == 0:
                if end - start < length:
                    length = end - start
                    ans = s[start:end]
                
                char = s[start]
                if char in total: 
                    total[char] += 1
                    if total[char] > 0:
                        counter += 1
                start += 1
                
        return ans if ans else ""