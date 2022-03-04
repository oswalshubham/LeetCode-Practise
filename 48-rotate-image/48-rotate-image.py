class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)
        
        
    def transpose(self, matrix : List[List[int]]):
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
    def reflect(self, matrix : List[List[int]]):
        n = len(matrix)
        for i in range(n):
            p=0
            q=n-1
            
            while q-p >=1:
                matrix[i][p],matrix[i][q] = matrix[i][q],matrix[i][p]
                p+=1
                q-=1
                
        