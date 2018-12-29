class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        totalWater = 0
        if not height:
            return totalWater
        
        leftHighest = [0]*(len(height)+1)
        leftHighest[0] = 0
        for i in range(len(height)):
            leftHighest[i+1] = max(leftHighest[i], height[i])
        
        rightHighest = 0
        for i in range(len(height)-1, 0, -1):
            rightHighest = max(rightHighest, height[i])
            if min(leftHighest[i], rightHighest) > height[i]:
                totalWater += min(leftHighest[i], rightHighest) - height[i]
                
        return totalWater