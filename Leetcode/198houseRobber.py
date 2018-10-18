class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = [0]*len(nums)
        ans[0] = nums[0]
        for i in range(1,len(nums)):
            ans[i] = max(ans[i-1], ans[i-2] + nums[i])
        return(ans[-1])