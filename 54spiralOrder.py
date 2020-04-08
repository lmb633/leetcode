class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        min_ = min(m, n)
        k = 0
        result = []
        while min_ - 2 * (k) > 0:
            for i in range(k, n - k):
                result.append(matrix[k][i])
            for i in range(k + 1, m - 1 - k):
                result.append(matrix[i][n - 1 - k])
            if m - 1 - k > k:
                for i in range(n - 1 - k, k - 1, -1):
                    result.append(matrix[m - 1 - k][i])
            if n - 1 - k > k:
                for i in range(m - 2 - k, k, -1):
                    result.append(matrix[i][k])
            k += 1
        return result
