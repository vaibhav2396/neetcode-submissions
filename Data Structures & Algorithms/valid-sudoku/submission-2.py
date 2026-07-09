class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validRow(i):
            rowCount = defaultdict(int)
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if rowCount[board[i][j]] == 1:
                    return False
                rowCount[board[i][j]] += 1
            return True
        
        def validCol(j):
            colCount = defaultdict(int)
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if colCount[board[i][j]] == 1:
                    return False
                colCount[board[i][j]] += 1
            return True
        
        def validBox(row,col):
            boxCount = defaultdict(int)
            for i in range(row,row+3):
                for j in range(col, col+3):
                    if board[i][j] == ".":
                        continue
                    if boxCount[board[i][j]] == 1:
                        return False
                    boxCount[board[i][j]] += 1

            return True 
        
        for i in range(9):
            if not(validRow(i) and validCol(i)):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not validBox(i,j):
                    return False
        return True
        
                    
        