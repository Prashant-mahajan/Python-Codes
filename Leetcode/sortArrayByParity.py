class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        e, o = [] , []
        for i in A:
            e.append(i) if i % 2 else o.append(i)
        return (o + e)                