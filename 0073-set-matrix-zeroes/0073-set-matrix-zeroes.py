class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row = False
        first_col = False

        #checking if first row has zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True
                break
        #checking if first column has zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break

        #starting (1,1) if any element is zero, setting respective index in first row and first col to zero
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        #filling zeroes
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        #filling first row if first_row
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        if first_col:
            for i in range(m):
                matrix[i][0] = 0

        

        