class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Iterative DFS approach, marking visited nodes
        
        visited = [0]*n
        ans = 0
        
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        for i in range(n):  
            if not visited[i]:
                ans += 1
                stack = [i]
                
                while(stack):
                    current = stack.pop()
                    visited[current] = 1
                    
                    if current in g: 
                        for neighbour in g[current]: 
                            if not visited[neighbour]:
                                stack.append(neighbour)
        return ans 