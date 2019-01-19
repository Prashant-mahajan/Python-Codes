from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ans = []
        if len(words) == 0 or len(s) == 0 or len(words[0]) == 0:
            return ans
        
        word_size = len(words[0])
        window_size = len(words)*word_size
        
        # Create table of frequency 
        table = collections.defaultdict(int) 
        for word in words:
            table[word] += 1

        for i in range(min(word_size, len(s)-window_size+1)):
            
            tmptable = {}
            start, end = i, i
            
            while end+word_size <= len(s):
                endchar = s[end: end+word_size]
                end = end + word_size
                
                if endchar not in table:
                    start = end
                    tmptable.clear()

                else:
                    tmptable[endchar] = tmptable[endchar] + 1 if endchar in tmptable else 1
                    
                    while tmptable[endchar] > table[endchar]:
                        tmptable[s[start:start+word_size]] -= 1
                        start = start + word_size
                    
                    if end - start == window_size:
                        ans.append(start)
        return ans
                
                
        