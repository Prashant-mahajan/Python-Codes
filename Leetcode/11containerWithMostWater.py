class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Brute Force solution results in TLE
        max_area = 0
        for i in range(len(height)+1):
            for j in range(i+1, len(height)):
                max_area = max(max_area, (j -i)*min(height[i],height[j]))
        return max_area
        
        # Revised solution
        area = 0 
        left = 0  
        right = len(height)-1
        while(left < right):
            area = max(area, (right - left)*min(height[left],height[right]))
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        return area