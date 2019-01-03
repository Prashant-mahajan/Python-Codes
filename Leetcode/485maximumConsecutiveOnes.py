class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                ans = max(count, ans)
                continue 
            else:
                count = 0
        return ans 