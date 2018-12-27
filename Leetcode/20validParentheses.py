class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {'}':'{', ')':'(', ']':'['}
        brackets = ['{', '(', '[']
        stack = []
        
        for i in s:
            if i in brackets:
                stack.append(i)
                continue
            if not stack or stack.pop() != pairs[i]:
                return False
        return not stack