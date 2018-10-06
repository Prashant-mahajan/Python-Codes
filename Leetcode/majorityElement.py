# Problem : https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # 1. Using dictionary
    nums_dict = {}
    for i in nums:  
        if i not in nums_dict:
            nums_dict[i] = 1 
        if nums_dict[i] > len(nums)/2:
            return i
        else:
            nums_dict[i] +=  1

    # 2. Voting Algorithm
    count, candidate = 0, 0
    for i in nums:
        if i == candidate:
            count += 1
        elif count == 0:
            candidate, count = i, 1
        else:
            count = count -1
        return candidate

    # 3. Sorting method
    nums.sort()
    length = len(nums)
    return nums[length//2]