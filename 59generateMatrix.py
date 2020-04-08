class Solution:
    def generateMatrix(self, n):
        if n <= 0:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        k = 0
        j = 1
        while n - 2 * k > 0:
            for i in range(k, n - k):
                matrix[k][i] = j
                j += 1
            for i in range(k + 1, n - 1 - k):
                matrix[i][n - 1 - k] = j
                j += 1
            if n - 1 - k > k:
                for i in range(n - 1 - k, k - 1, -1):
                    matrix[n - 1 - k][i] = j
                    j += 1
            if n - 1 - k > k:
                for i in range(n - 2 - k, k, -1):
                    matrix[i][k] = j
                    j += 1
            k += 1
        return matrix


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(5))
