class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int: 
        matrix = [[True for i in range(n)] for j in range(m)]
        directions = [(0,-1),(0,1),(1,0),(-1,0)]
        for i,j in walls:
            matrix[i][j] = None
            
        def checkInDirection(i,j,l,r, memo = {}):
            new_l = i+l
            new_r = j+r
            
            if (new_l,new_r,l,r) in memo:
                return None
            if new_l >=0 and new_r >=0 and new_l<m and new_r<n:
                if matrix[new_l][new_r]==True:
                    matrix[new_l][new_r] = False
                elif matrix[new_l][new_r] == None:
                    return None
                memo[(new_l,new_r,l,r)] = True
                checkInDirection(new_l,new_r,l,r, memo)
                
                    
            else:
                return None
        
        memo = {}
        for i,j in guards:
            matrix[i][j] = False
            for l,r in directions:
                checkInDirection(i,j,l,r, memo)
        count = 0      
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == True:
                    count+=1
                    
        return count
                    
                    
                
                
        
                    
        
            