import queue


class Solution(object):
    def orangesRotting(self, grid):
        result = 0
        row = len(grid)
        col = len(grid[0])
        q = queue.Queue()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.put((i, j))
        # print(q.qsize())
        while not q.empty():
            q2 = queue.Queue()
            while not q.empty():
                i, j = q.get()
                # print(i,j)
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    q2.put((i - 1, j))
                if i + 1 < row and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    q2.put((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    q2.put((i, j - 1))
                if j + 1 < col and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    q2.put((i, j + 1))
            q = q2
            # print(q.qsize())
            if not q.empty():
                result += 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return result


solution = Solution()
a = [[1,2]]
print('result', solution.orangesRotting(a))
