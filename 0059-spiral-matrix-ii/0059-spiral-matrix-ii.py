class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row_start, col_start = 0,0
        row_end = n-1
        col_end = n-1

        result = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        while row_start<=row_end and col_start<=col_end:
            #travel east
            for i in range(col_start,col_end+1):
                result[row_start][i]= count
                count+=1

            row_start+=1
            
            #travel south

            for i in range(row_start, row_end+1):
                result[i][col_end] = count
                count+=1
            
            col_end -=1
            
            #travel west
            
            for i in range(col_end, col_start-1,-1):
                result[row_end][i]=count
                count+=1
                
            row_end-=1
            
            #travel north
            
            for i in range(row_end, row_start-1,-1):
                result[i][col_start]= count
                count+=1
                
            col_start+=1

        return result

        