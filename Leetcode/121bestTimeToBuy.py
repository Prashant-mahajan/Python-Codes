class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Approach 1: 
        min_, max_ = float('inf'), 0
        for i in prices:
            min_ = min(i, min_)
            profit = i - min_
            max_ = max(profit, max_)
        return max_


        # Approach 2 
        if not prices:
            return 0           
            
        profit, min_ = 0, prices[0]
        for i in prices[1:]:
            if i < min_:
                min_ = i

            elif i - min_ > profit:
                profit = i - min_

        return profit

