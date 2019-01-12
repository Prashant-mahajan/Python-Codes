class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.explore(sorted(candidates), 0, target, result,[])
        return result
    
    def explore(self, candidates, index, target, result,path):
        if target is 0:
            result.append(path)
            return
        
        if target < 0:
            return 
    
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            self.explore(candidates, i+1, target-candidates[i], result,path+[candidates[i]])