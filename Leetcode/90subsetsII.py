class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(sorted(nums), [], 0, result)
        return result
    
    def dfs(self, nums, path, index, result):
        result.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, path + [nums[i]], i+1, result)
            