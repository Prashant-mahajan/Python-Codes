class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, columns = len(M), len(M[0])
        add = [[0]*columns for _ in M]
        
        for i in range(rows):
            for j in range(columns):
                count = 0
                
                for a in (i-1, i, i+1):
                    for b in (j-1, j, j+1):
                        if 0 <= a < rows and 0 <= b < columns:
                            add[i][j] += M[a][b]
                            count += 1
                add[i][j] /= count
        return add
                