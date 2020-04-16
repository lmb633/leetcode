import heapq


class Solution:
    def trapRainWater(self, height_map):
        m = len(height_map)
        n = len(height_map[0])
        heap = []
        visited = set()
        for i in range(m):
            heapq.heappush(heap, (height_map[i][0], i, 0))
            visited.add((i, 0))
            heapq.heappush(heap, (height_map[i][n - 1], i, n - 1))
            visited.add((i, n - 1))
        for j in range(1, n - 1):
            heapq.heappush(heap, (height_map[0][j], 0, j))
            visited.add((0, j))
            heapq.heappush(heap, (height_map[m - 1][j], m - 1, j))
            visited.add((m - 1, j))
        result = 0
        neighbor = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        while heap:
            heigh, i, j = heapq.heappop(heap)
            # print(heigh, i, j)
            for x, y in neighbor:
                x = i + x
                y = j + y
                if (x, y) not in visited and 0 <= x < m and 0 <= y < n:
                    # print(x,y)
                    if height_map[x][y] < height_map[i][j]:
                        result += height_map[i][j] - height_map[x][y]
                        height_map[x][y] = height_map[i][j]
                    heapq.heappush(heap, (height_map[x][y], x, y))
                    visited.add((x, y))
        return result


if __name__ == '__main__':
    test = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
    solution = Solution()
    print(solution.trapRainWater(test))
