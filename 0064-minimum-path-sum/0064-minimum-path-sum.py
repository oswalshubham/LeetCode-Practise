class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        columns = len(grid[0])

        min_sum = float('inf')

        directions = [(1,0),(0,1)]
        memo = [[-1 for _ in range(columns)] for _ in range(rows)]

        def dfs(x,y, memo):
            if 0 <= x < rows and 0 <= y < columns:
                if memo[x][y]!=-1:
                    return memo[x][y]

                if x == rows-1 and y == columns-1:
                    return grid[x][y]
                
                memo[x][y] =  grid[x][y] + min(dfs(x,y+1, memo), dfs(x+1,y, memo))
                return memo[x][y]

            else:
                return float('inf')

        

        return dfs(0,0, memo)