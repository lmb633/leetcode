class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            if not self.isvalid_row(board, i) or not self.isvalid_column(board, i):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isvalid_square(board, i, j):
                    return False
        return True

    def isvalid_square(self, board, index1, index2):
        validset = set()
        for i in range(3):
            for j in range(3):
                val = board[index1 * 3 + i][index2 * 3 + j]
                if val == '.' or val not in validset:
                    validset.add(val)
                else:
                    return False
        return True

    def isvalid_row(self, board, index):
        validset = set()
        for i in range(9):
            val = board[index][i]
            if val == '.' or val not in validset:
                validset.add(val)
            else:
                return False
        return True

    def isvalid_column(self, board, index):
        validset = set()
        for i in range(9):
            val = board[i][index]
            if val == '.' or val not in validset:
                validset.add(val)
            else:
                return False
        return True


sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
solution = Solution()
print(solution.isValidSudoku(sudoku))
