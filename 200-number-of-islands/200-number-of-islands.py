class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]=="1":
                grid[i][j] = "#" 
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
                    
        return count
                
        