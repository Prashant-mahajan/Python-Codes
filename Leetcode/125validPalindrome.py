class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join([i for i in s if i.isalnum()])
        j = len(s) - 1
        i = 0
        while i < j:
            if s[i] != s[j]:
                return False
            j -= 1
            i += 1
        return True 