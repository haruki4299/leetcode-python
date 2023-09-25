class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate Rows
        for i in range(9):
            seen = []
            row = board[i]
            for j in range(9):
                if row[j] not in seen or row[j] == '.':
                    seen.append(row[j])
                else:
                    return False
        print("rows are fine")

        # Validate Columns
        for i in range(9):
            seen = []
            for j in range(9):
                if board[j][i] not in seen or board[j][i] == '.':
                    seen.append(board[j][i])
                else:
                    return False
        print("columns are fine")
        # Validate Squares
        for i in range(3):
            for j in range(3):
                seen = []
                print(i,j)
                for x in range(3):
                    for y in range(3):
                        print(seen)
                        if board[3*i + x][3*j + y] not in seen or board[3*i + x][3*j + y] == '.':
                            seen.append(board[3*i + x][3*j + y])
                        else:
                            return False
        return True
                        

                    
