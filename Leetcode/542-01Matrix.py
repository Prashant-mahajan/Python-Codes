class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        """ Perform BFS  
        1. iterate through all 0's in the matrix 
        2. Start a recursive call at these cells after updating their neighbours by 1 
        3. Stop only if the cell under consideration is already closer to another 0.
        """

        queue = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                else:
                    matrix[i][j] = sys.maxsize
        
        for i, j in queue:
            for r, c in ((i,j+1), (i, j-1), (i-1,j), (i+1,j)):
                update = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and update < matrix[r][c]:
                    matrix[r][c] = update
                    queue.append((r,c))

        return matrix