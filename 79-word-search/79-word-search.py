class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,index,visited = []):
            if index == len(word):
                return True
            if i>=0 and i < len(board) and j>=0 and j<len(board[0]) and board[i][j] == word[index]:
                temp = board[i][j]
                board[i][j] = "#"
                right = dfs(i,j+1,index+1,visited)
                left = dfs(i,j-1, index+1,visited)
                up = dfs(i-1,j,index+1,visited)
                down = dfs(i+1,j,index+1,visited)
                
                res = left or right or up or down
                board[i][j] = temp
                return res
                
            else:
                return False
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = []
                    result = dfs(i,j,0, visited)
                    if result == True:
                        return True
                    
        return False
            
        