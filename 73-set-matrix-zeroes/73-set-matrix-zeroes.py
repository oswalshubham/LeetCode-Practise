class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero = [False]*len(matrix)
        colZero = [False]*len(matrix[0])
        
        zeroPos = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroPos.append((i,j))
                    
        for pos in zeroPos:
            if rowZero[pos[0]] == False:
                for j in range(len(matrix[0])):
                    matrix[pos[0]][j] = 0
                    
                rowZero[pos[0]] = True
                
            if colZero[pos[1]] == False:
                for i in range(len(matrix)):
                    matrix[i][pos[1]] = 0
                    
                colZero[pos[1]] = True