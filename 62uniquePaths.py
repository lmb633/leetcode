class Solution(object):
    def uniquePaths(self, m, n):
        solution = [0 for a in range(n)]
        f_i_j = -1
        for i in range(0, m):
            for j in range(0, n):
                print(f_i_j)
                if i == 0 or j == 0:
                    f_i_j = 1
                    solution[j] = 1
                else:
                    f_i_j = f_i_j + solution[j]
                    solution[j] = f_i_j
            print(solution)
        return f_i_j


solution = Solution()
print(solution.uniquePaths(7, 3))
