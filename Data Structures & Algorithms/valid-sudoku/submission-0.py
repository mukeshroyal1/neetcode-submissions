class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp = []
        check = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
        def isSquare(j, i):
            temp = []
            if board[j][i] != '.':
                    temp.append(int(board[j][i]))
            if board[j+1][i+1] != '.':
                    temp.append(int(board[j+1][i+1]))
            if board[j][i+1] != '.':
                    temp.append(int(board[j][i+1]))
            if board[j-1][i+1] != '.':
                    temp.append(int(board[j-1][i+1]))
            if board[j-1][i] != '.':
                    temp.append(int(board[j-1][i]))
            if board[j-1][i-1] != '.':
                    temp.append(int(board[j-1][i-1]))
            if board[j][i-1] != '.':
                    temp.append(int(board[j][i-1]))
            if board[j+1][i-1] != '.':
                    temp.append(int(board[j+1][i-1]))
            if board[j+1][i] != '.':
                    temp.append(int(board[j+1][i]))
            if len(temp) != len(set(temp)):
                return False 
            else:
                return True 
            
            
        for j in range(9):
            for i in range(9):
                if board[j][i] != '.':
                    temp.append(int(board[j][i]))
                if (j, i) in check:
                    if isSquare(j, i) == False:
                        return False 

            if len(temp) != len(set(temp)):
                return False 
            temp = []

        for j in range(9):
            for i in range(9):
                if board[i][j] == '.':
                    continue 
                else:
                    temp.append(int(board[i][j]))
            if len(temp) != len(set(temp)):
                return False 
            temp = []
        return True 
