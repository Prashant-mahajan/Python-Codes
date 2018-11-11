class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        """
        1. Reverse the matrix order
        2. Find the transpose using zip function
        """

        matrix[::] = zip(*matrix[::-1])
            
            