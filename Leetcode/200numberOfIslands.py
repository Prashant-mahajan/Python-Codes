class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Apply principal of finding number of strongly connected components in a graph
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    ans += 1
        return ans 
    
    def dfs(self, graph, y, x):   
        # Note the directions are reversed to adjust co-ordinate systems
        if 0 > x or x >= len(graph[0]) or 0 > y or y>= len(graph) or graph[y][x] != '1':
            return 
        graph[y][x] = '*'
        self.dfs(graph, y, x+1)
        self.dfs(graph, y+1, x)
        self.dfs(graph, y-1, x)
        self.dfs(graph, y, x-1)