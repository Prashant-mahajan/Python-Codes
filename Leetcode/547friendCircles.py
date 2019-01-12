class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Apply principal of finding number of strongly connected components in a graph
        friends = [0]*len(M)
        ans = 0
        stack = []
        
        for i in range(len(M)):
            if friends[i] == False:
                ans += 1
                stack.append(i)
            
            while(stack):
                current = stack.pop()
                friends[current] = True
                
                for j in range(len(M[current])):
                    if not friends[j] and M[current][j] == 1: 
                        stack.append(j)
        return ans 