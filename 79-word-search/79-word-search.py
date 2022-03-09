class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return True
        def dfs(i,j,index,visited = []):
            if index == len(word):
                return True
            if i>=0 and i < len(board) and j>=0 and j<len(board[0]) and board[i][j] == word[index]:
                temp = board[i][j]
                board[i][j] = "#"
                right = dfs(i,j+1,index+1)
                left = dfs(i,j-1, index+1)
                up = dfs(i-1,j,index+1)
                down = dfs(i+1,j,index+1)
                
                res = left or right or up or down
                board[i][j] = temp
                return res
                
            else:
                return False
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    result = dfs(i,j,0)
                    if result == True:
                        return True
                    
        return False
            
        