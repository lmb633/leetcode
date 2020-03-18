import copy


class Solution(object):
    def solveNQueens(self, n):
        queen = [['.' for i in range(n)] for j in range(n)]
        result = []

        def check(queen, x, y, n):
            if queen[x].count('Q') > 1:
                return False
            column = [queen[i][y] for i in range(n)]
            if column.count('Q') > 1:
                return False
            sum_ = x + y
            dig = []
            for i in range(sum_ + 1):
                if i < n and sum_ - i < n:
                    dig.append(queen[i][sum_ - i])
            if dig.count('Q') > 1:
                return False
            dig = []
            i, j = x, y
            while i < n and j < n:
                dig.append(queen[i][j])
                i += 1
                j += 1
            i, j = x - 1, y - 1
            while i >= 0 and j >= 0:
                dig.append(queen[i][j])
                i -= 1
                j -= 1
            if dig.count('Q') > 1:
                return False
            return True

        def helper(queen, i, j, left_num):
            if i >= n or j >= n or left_num < 0:
                return
            queen[i][j] = 'Q'
            # print(i, j)

            if check(queen, i, j, n):
                if left_num - 1 == 0:
                    result.append(copy.deepcopy(queen))
                else:
                    inext = add_i(i, n)
                    helper(queen, inext, 0, left_num - 1)
            queen[i][j] = '.'
            inext, jnext = add_i_j(i, j, n)
            helper(queen, inext, jnext, left_num)

        def helper2(queen, i, left):
            if i >= n:
                return
            for j in range(n):
                # print(i, j, left)
                queen[i][j] = 'Q'
                if check(queen, i, j, n):
                    if left - 1 == 0:
                        result.append(copy.deepcopy(queen))
                    helper2(queen, i + 1, left - 1)
                queen[i][j] = '.'

        def add_i_j(i, j, n):
            if j + 1 < n:
                return i, j + 1
            elif i + 1 < n:
                return i + 1, 0
            else:
                return n, n

        def add_i(i, n):
            if i + 1 < n:
                return i + 1
            else:
                return n

        # 剪枝不够，超时
        # helper(queen, 0, 0, n)
        helper2(queen, 0, n)
        return [[''.join(q) for q in qs] for qs in result]


solution = Solution()
print(len(solution.solveNQueens(1)))
