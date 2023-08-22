class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        '''
        [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]    
        '''
        def dfs(i,j, index, visited = set()):
            if index == len(word):
                return True

            if 0<=i<m and 0<=j<n and board[i][j] == word[index] and (i,j) not in visited:
                    visited.add((i,j))

                    left = dfs(i+1,j,index+1,visited)
                    down = dfs(i,j+1,index+1,visited)
                    right = dfs(i-1,j,index+1,visited)
                    up = dfs(i,j-1,index+1,visited)

                    visited.remove((i,j))
                    return (left or right or up or down)

            else:
                return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    answer = dfs(i,j,0,visited)

                    if answer:
                        return True

        return False

                

            


        
            
        