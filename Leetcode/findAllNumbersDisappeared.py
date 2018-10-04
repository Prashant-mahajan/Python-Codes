# Problem - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [i for i in range(1,len(nums)+1)]
        nums_dict = set(nums)
        return list(set(ans) - set(nums_dict))

        
        