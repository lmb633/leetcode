class Solution(object):
    def rotate(self, matrix):
        k = 0
        lenght = len(matrix)
        while lenght - 2 * (k + 1) >= 0:
            for i in range(lenght - 2 * (k + 1) + 1):
                temp = matrix[k][k + i]
                matrix[k][k + i] = matrix[lenght - 1 - k - i][k]
                matrix[lenght - 1 - k - i][k] = matrix[lenght - 1 - k][lenght - 1 - k - i]
                matrix[lenght - 1 - k][lenght - 1 - k - i] = matrix[k + i][lenght - 1 - k]
                matrix[k + i][lenght - 1 - k] = temp
            k += 1
        return matrix
