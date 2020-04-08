import queue


# 笨方法 BFS逐个遍历
class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = []
        succeed = set()
        points = self.cicle(matrix)
        for i, j in points:
            print(i, j)
            if self.helper(matrix, i, j, m - 1, n - 1, succeed):
                print(True)
                result.append([i, j])
                succeed.add((i, j))
        return result

    def helper(self, matrix, i, j, m, n, succeed):

        flag1 = False
        flag2 = False
        visited = set()
        visited.add((i, j))
        q = queue.Queue()
        q.put((i, j))
        while q.qsize() > 0:
            x, y = q.get()
            if x - 1 < 0 or y - 1 < 0:
                flag1 = True
            if x + 1 > m or y + 1 > n:
                flag2 = True
            if flag2 and flag1:
                return True
            if x - 1 >= 0 and matrix[x - 1][y] <= matrix[x][y] and (x - 1, y) not in visited:
                if (x - 1, y) in succeed:
                    return True
                visited.add((x - 1, y))
                q.put((x - 1, y))
            if y - 1 >= 0 and matrix[x][y - 1] <= matrix[x][y] and (x, y - 1) not in visited:
                if (x, y - 1) in succeed:
                    return True
                visited.add((x, y - 1))
                q.put((x, y - 1))
            if x + 1 <= m and matrix[x + 1][y] <= matrix[x][y] and (x + 1, y) not in visited:
                if (x + 1, y) in succeed:
                    return True
                visited.add((x + 1, y))
                q.put((x + 1, y))
            if y + 1 <= n and matrix[x][y + 1] <= matrix[x][y] and (x, y + 1) not in visited:
                if (x, y + 1) in succeed:
                    return True
                visited.add((x, y + 1))
                q.put((x, y + 1))
        return False

    # 从边上开始遍历  时间也没提升多少
    def cicle(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        min_ = min(m, n)
        k = 0
        result = []
        while min_ - 2 * k > 0:
            for i in range(k, n - k):
                result.append((k, i))
            for i in range(k + 1, m - 1 - k):
                result.append((i, n - 1 - k))
            if m - 1 - k > k:
                for i in range(n - 1 - k, k - 1, -1):
                    result.append((m - 1 - k, i))
            if n - 1 - k > k:
                for i in range(m - 2 - k, k, -1):
                    result.append((i, k))
            k += 1
        return result


class Solution2():
    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]:
            return []
        pac = set()
        atl = set()
        m = len(matrix)
        n = len(matrix[0])

        def helper(i, j, visited):
            visited.add((i, j))
            add_ = [[0, -1], [-1, 0], [0, 1], [1, 0]]
            for x, y in add_:
                x = i + x
                y = j + y
                if 0 <= x < m and 0 <= y < n and matrix[x][y] >= matrix[i][j] and (x, y) not in visited:
                    helper(x, y, visited)

        for i in range(m):
            helper(i, 0, pac)
        for i in range(n):
            helper(0, i, pac)
        for i in range(m):
            helper(i, n - 1, atl)
        for i in range(n):
            helper(m - 1, i, atl)
        return pac & atl


if __name__ == '__main__':
    # a = [[1, 2, 3, 4, 5],
    #      [16, 17, 18, 19, 6],
    #      [15, 24, 25, 20, 7],
    #      [14, 23, 22, 21, 8],
    #      [13, 12, 11, 10, 9]]
    a = [[19, 16, 16, 12, 14, 0, 17, 11, 2, 0, 18, 9, 13, 16, 8, 8, 8, 13, 17, 9, 16, 9, 4, 7, 1, 19, 10, 7, 0, 15],
         [0, 11, 4, 14, 9, 0, 6, 13, 16, 5, 19, 9, 4, 5, 4, 12, 0, 13, 0, 7, 9, 12, 13, 15, 3, 7, 4, 9, 15, 1],
         [13, 14, 12, 12, 12, 16, 6, 15, 13, 1, 8, 9, 11, 14, 14, 10, 19, 11, 10, 0, 5, 18, 4, 12, 7, 13, 17, 15, 18, 1],
         [16, 14, 19, 5, 8, 2, 11, 17, 7, 1, 4, 6, 5, 18, 7, 15, 6, 19, 18, 12, 1, 14, 2, 2, 0, 9, 15, 14, 13, 19],
         [17, 4, 12, 9, 12, 10, 12, 10, 4, 5, 12, 7, 2, 12, 18, 10, 10, 8, 6, 1, 5, 13, 10, 3, 5, 3, 11, 4, 8, 11],
         [8, 19, 18, 9, 6, 2, 7, 3, 19, 6, 0, 17, 9, 12, 11, 1, 15, 11, 18, 1, 8, 11, 1, 11, 16, 7, 8, 17, 15, 0],
         [7, 0, 5, 11, 1, 7, 12, 18, 12, 1, 5, 2, 11, 7, 18, 12, 0, 11, 9, 18, 5, 2, 3, 1, 1, 1, 8, 14, 19, 5],
         [2, 14, 2, 16, 17, 19, 10, 16, 1, 16, 16, 3, 19, 12, 13, 17, 19, 12, 16, 10, 16, 8, 16, 12, 6, 12, 13, 17, 9, 12],
         [8, 1, 10, 5, 7, 0, 15, 19, 8, 15, 4, 12, 18, 18, 13, 11, 5, 2, 8, 3, 15, 4, 3, 7, 7, 14, 15, 11, 6, 16],
         [0, 5, 13, 19, 1, 1, 2, 4, 16, 2, 16, 9, 15, 15, 10, 10, 18, 11, 17, 1, 5, 14, 5, 19, 7, 0, 13, 7, 13, 7],
         [11, 6, 16, 12, 4, 2, 9, 11, 17, 19, 12, 10, 6, 16, 17, 5, 1, 18, 19, 7, 15, 1, 14, 0, 3, 19, 7, 3, 4, 13],
         [4, 11, 8, 10, 10, 19, 7, 18, 4, 2, 2, 14, 6, 9, 18, 14, 2, 16, 5, 3, 19, 17, 4, 3, 7, 1, 12, 2, 4, 3],
         [14, 16, 3, 11, 13, 13, 6, 16, 18, 0, 17, 19, 4, 1, 14, 12, 4, 17, 5, 19, 8, 13, 15, 3, 15, 4, 1, 14, 12, 10],
         [13, 2, 12, 2, 16, 12, 19, 10, 19, 12, 19, 14, 12, 17, 16, 3, 13, 7, 3, 15, 16, 7, 10, 15, 14, 10, 6, 5, 2, 18]]
    solution = Solution2()
    print(solution.pacificAtlantic(a))
