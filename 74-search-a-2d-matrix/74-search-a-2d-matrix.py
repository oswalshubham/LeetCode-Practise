class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        column = 0
        
        while row < len(matrix):
            if row < len(matrix)-1 and target >= matrix[row+1][column]:
                row+=1
                continue
            else:
                while column < len(matrix[0]):
                    if matrix[row][column] == target:
                        return True
                    else:
                        column+=1
                        
                return False
            
