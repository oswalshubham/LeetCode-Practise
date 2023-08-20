class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row_s,row_e = 0,m-1
        row_pos = -1

        while row_s <= row_e:
            mid = row_s + (row_e - row_s)//2

            if matrix[mid][0] <= target <= matrix[mid][n-1]:
                row_pos = mid
                break
            
            elif matrix[mid][0] > target:
                row_e = mid-1
            
            else:
                row_s = mid+1

        
        if row_pos == -1:
            return False

        
        col_s, col_e = 0,n-1

        while col_s <= col_e:
            mid = col_s + (col_e-col_s)//2

            if matrix[row_pos][mid] == target:
                return True
            
            elif matrix[row_pos][mid] > target:
                col_e = mid-1
            else:
                col_s = mid+1

        return False



            
