class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        array = [0]*8

        for i in range(len(moves)):
            player = "A" if i%2==0 else "B"

            row,column = moves[i]

            if player == "A":
                sign = 1
            elif player == "B":
                sign = -1
                
            array[row]+=sign
            array[column+3]+=sign

            if row == column:
                array[6]+=sign
                
            if column == 2-row:
                array[7]+=sign

        
        for i in range(len(array)):
            if array[i] == 3:
                return "A"
            
            elif array[i] == -3:
                return "B"

        return "Draw" if len(moves)==9 else "Pending" 

