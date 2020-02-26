# 该解法保存一个列数组或者行数组，内存为m或者n，一般解法内存为m*n
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        solution = [0 for a in range(n)]
        f_i_j = 1
        for i in range(0, m):
            for j in range(0, n):
                if i == 0:
                    if obstacleGrid[i][j] == 1:
                        f_i_j = 0
                        solution[j] = 0
                    else:
                        f_i_j = f_i_j
                        solution[j] = f_i_j
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        f_i_j = 0
                        solution[j] = 0
                    else:
                        f_i_j = solution[j]
                        solution[j] = f_i_j
                else:
                    if obstacleGrid[i][j] == 1:
                        f_i_j = 0
                        solution[j] = 0
                    else:
                        f_i_j = f_i_j + solution[j]
                        solution[j] = f_i_j
            print(solution)
        return f_i_j


a = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
solution = Solution()
print(solution.uniquePathsWithObstacles(a))
