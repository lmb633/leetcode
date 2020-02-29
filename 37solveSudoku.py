class Solution:
    def __init__(self):
        self.flag = True

    def solveSudoku(self, board):
        self.solve(board, 0, 0)

    def solve(self, board, i, j):
        while board[i][j] != '.':
            if j < 8:
                j += 1
            elif i < 8:
                i += 1
                j = 0
            else:
                self.flag = False
                return
        if board[i][j] == '.':
            for num in [str(idx) for idx in range(1, 10)]:
                if not self.flag:
                    return
                board[i][j] = num
                # print(i, j, num, board)
                if self.isvalid(board, i, j):
                    if i == 8 and j == 8:
                        self.flag = False
                        return
                    if j == 8 and i < 8:
                        self.solve(board, i + 1, 0)
                    else:
                        self.solve(board, i, j + 1)
                if self.flag != False:
                    board[i][j] = '.'

    def isvalid(self, board, i, j):
        return self.isvalid_row(board, i) and self.isvalid_column(board, j) and self.isvalid_square(board, i // 3, j // 3)

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


#
sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
          [".", "9", "8", ".", ".", ".", ".", "6", "."],
          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
          [".", "6", ".", ".", ".", ".", "2", "8", "."],
          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# sudoku = [["5", ".", "4", "6", "7", "8", "9", "1", "2"],
#           ["6", "7", ".", ".", "9", "5", "3", "4", "8"],
#           ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#           ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#           ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#           ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#           ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#           ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#           ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
solution = Solution()
solution.solveSudoku(sudoku)
print(sudoku)
