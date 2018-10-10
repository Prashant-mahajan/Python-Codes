class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 
        
        current, maximum = nums[0], nums[0]
        for i in nums[1:]:
            current = max(i, current+i)
            maximum = max(current, maximum)

        return maximum
    
        # Kadane's algorithm which fails for negative values
        # if add + i <= 0:
        #     add = 0
        # else:
        #     add += i
        #     #print (add)
        # ans = max(ans, add)
        