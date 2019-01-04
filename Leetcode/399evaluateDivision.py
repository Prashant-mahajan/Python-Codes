class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Sets a default value if item is not present in the dictionary
        ans = collections.defaultdict(dict)

        # zip binds the value from two variables together
        for (num, den), val in zip(equations, values):
            ans[num][num] = ans[den][den] = 1.0
            ans[num][den] = val
            ans[den][num] = 1 / val
        
        # Get all possible permutations 
        for k, i, j in itertools.permutations(ans,3):
            if k in ans[i] and j in ans[k]:
                ans[i][j] = ans[i][k] * ans[k][j]
                
        return  [ans[num].get(den, -1.0) for num, den in queries]
    

