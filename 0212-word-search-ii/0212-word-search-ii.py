class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        
        m = len(board)
        n = len(board[0])

        for word in words:
            root = trie
            for char in word:
                if char not in root.children:
                    root.children[char] = TrieNode()
                
                root = root.children[char]

            root.isEnd = True

        
        def dfs(i,j,root, result = "", answer = []):

            if 0<=i<m and 0<=j<n and board[i][j] in root.children:
                char = board[i][j]
                result+= char

                board[i][j] = "#"

                if root.children[char].isEnd:
                    answer.append(result)

                dfs(i+1,j,root.children[char], result, answer)
                dfs(i,j+1,root.children[char], result, answer)
                dfs(i-1,j,root.children[char], result, answer)
                dfs(i,j-1,root.children[char], result, answer)

                result = result[:-1]
                board[i][j] = char


        root = trie
        answer = []

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(i,j,root,"", answer)

        
        return list(set(answer))

