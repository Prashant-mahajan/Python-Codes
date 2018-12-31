class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str, digits)))
        num += 1
        ans = [int(d) for d in str(num)]
        return ans 
                