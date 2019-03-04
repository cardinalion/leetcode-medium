class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[],[],[],[],[],[],[],[],[]]
        col = [[],[],[],[],[],[],[],[],[]]
        group = [[],[],[],[],[],[],[],[],[]]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                else:
                    row[i].append(board[i][j])
                if board[i][j] in col[j]:
                    return False
                else:
                    col[j].append(board[i][j])
                k = int((i/3))*3+int(j/3)
                if board[i][j] in group[k]:
                    return False
                else:
                    group[k].append(board[i][j])
        return True
