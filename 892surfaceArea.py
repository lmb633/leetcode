class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        result = 0

        def check(i, j, i0, j0):
            if i0 < 0 or i0 >= n or j0 < 0 or j0 >= n:
                return grid[i][j]
            elif grid[i][j] > grid[i0][j0]:
                return grid[i][j] - grid[i0][j0]
            else:
                return 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    cur = 0
                else:
                    cur = 2
                    cur += check(i, j, i - 1, j)
                    cur += check(i, j, i + 1, j)
                    cur += check(i, j, i, j - 1)
                    cur += check(i, j, i, j + 1)
                result += cur
        return result

        """
        :type grid: List[List[int]]
        :rtype: int
        """