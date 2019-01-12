class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.explore(candidates, 0, target, result,[])
        return result
    
    def explore(self, candidates, index, target, result,path):
        if target is 0:
            result.append(path)
            return
        
        if target < 0:
            return 
    
        for i in range(index, len(candidates)):
            self.explore(candidates, i, target-candidates[i], result,path+[candidates[i]])