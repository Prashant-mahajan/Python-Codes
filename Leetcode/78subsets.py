class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, [], 0, result)
        return result
    
    def dfs(self, nums, path, index, result):
        result.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, path+[nums[i]], i+1, result)

