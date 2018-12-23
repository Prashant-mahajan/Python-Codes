class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        k = l = 0
        ans = []
        if len(matrix) == 0:
            return ans
        m, n = len(matrix), len(matrix[0])

        
        while(k<m and l<n):
            # Print first row
            for i in range(l,n):
                ans.append(matrix[k][i])
            k += 1 

            # Print last column
            for i in range(k,m):
                ans.append(matrix[i][n-1])
            n -= 1

            # Print last row
            if k < m:
                for i in range(n-1, l-1, -1):
                    ans.append(matrix[m-1][i])
                m -= 1
            
            # Print first column
            if l < n:
                for i in range(m-1, k-1, -1):
                    ans.append(matrix[i][l])
                l += 1
        
        return ans
                
        
        