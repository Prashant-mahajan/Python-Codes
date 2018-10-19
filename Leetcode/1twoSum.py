class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return 
  
        save = {}
        for i in range(len(nums)):
            if target - nums[i] in save:
                return [save[target-nums[i]], i]
            else: 
                save[nums[i]] = i
                
        
        
