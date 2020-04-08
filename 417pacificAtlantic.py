import queue


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


if __name__ == '__main__':
    a = [[1, 2, 3, 4, 5],
         [16, 17, 18, 19, 6],
         [15, 24, 25, 20, 7],
         [14, 23, 22, 21, 8],
         [13, 12, 11, 10, 9]]
    # a = [[1, 2],
    #      [3, 4]]
    solution = Solution()
    print(solution.pacificAtlantic(a))
