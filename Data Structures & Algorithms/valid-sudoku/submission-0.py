class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for row in board:
            rowSet = set()
            for num in row:
                if num != "." and int(num) not in rowSet:
                    rowSet.add(int(num))
                elif num != "." and int(num) in rowSet:
                    return False
        for i in range(len(board[0])):
            colSet = set()
            for j in range(len(board)):
                if board[j][i] != "." and int(board[j][i]) not in colSet:
                    colSet.add(int(board[j][i]))
                elif board[j][i] != "." and int(board[j][i]) in colSet:
                    return False
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                boxSet = set()
                for rowInd in range(row, row + 3):
                    for colInd in range(col, col + 3):
                        if board[rowInd][colInd] != "." and int(board[rowInd][colInd]) not in boxSet:
                            boxSet.add(int(board[rowInd][colInd]))
                        elif board[rowInd][colInd] != "." and int(board[rowInd][colInd]) in boxSet:
                            return False
        return True