# Problem - https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Using Dictionaries
        num_dict = dict([i, nums.count(i)] for i in nums)
        for key, value in num_dict.items():
            if value == 1:
                return key
        
        # Using concept of XOR 
        number = 0
        for i in nums:
            number = number ^ i 
        return number 
            