class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        result = []

        rowS, rowE = rStart, rStart
        colS, colE = cStart, cStart

        while True:
            for i in range(colS, colE+1):
                if 0<=rowS<rows and 0<=i<cols:
                    result.append([rowS,i])

            colE+=1

            for i in range(rowS, rowE+1):
                if 0<=i<rows and 0<=colE<cols:
                    result.append([i,colE])

            rowE+=1

            for i in range(colE, colS-1,-1):
                if 0<=rowE<rows and 0<=i<cols:
                    result.append([rowE,i])

            colS-=1

            for i in range(rowE, rowS-1,-1):
                if 0<=i<rows and 0<=colS<cols:
                    result.append([i,colS])

            rowS-=1

            if len(result) == rows*cols:
                break

        return result
        