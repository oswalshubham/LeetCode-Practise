from collections import defaultdict
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
                return []
    
        pacific = set()
        atlantic = set()
        m,n = len(matrix), len(matrix[0])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        
        def dfs(visited, x,y):
            visited.add((x,y))
            for dx, dy in directions:
                new_x, new_y  = x + dx, y + dy

                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited and matrix[new_x][new_y] >= matrix[x][y]:
                    dfs (visited, new_x, new_y)

                    
        for i in range(m):
            dfs(pacific, i , 0)
            dfs(atlantic, i, n-1)

        for j in range(n):
            dfs(pacific, 0 , j)
            dfs(atlantic, m-1, j)

        return list(pacific.intersection(atlantic))
        
        
        