class Solution(object):
    def movingCount(self, m, n, k):
        def check(i, j):
            return i % 10 + 1 // 10 + j % 10 + j // 10

        visited = set()
        stack = []
        stack.append((0, 0))
        visited.add((0, 0))
        step = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while stack:
            i, j = stack.pop()
            for x, y in step:
                x = i + x
                y = j + y
                if 0 <= x <= m and 0 <= y <= n and check(x, y) <= k:
                    if (x, y) not in visited:
                        visited.add((x, y))
                        stack.append((x, y))
        return len(visited)
