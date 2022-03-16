class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j,visited):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return None
            if (i,j) not in visited:
                if grid[i][j] == "0":
                    return None
                else:
                    visited[(i,j)] = True
                    
                    dfs(i+1,j,visited)
                    dfs(i-1,j,visited)
                    dfs(i,j+1,visited)
                    dfs(i,j-1,visited)
            else:
                return None
                    
        visited = {}
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j,visited)
                    count+=1
                    
        return count
                
        