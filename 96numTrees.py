# 递归超时
class Solution:
    def numTrees(self, n: int) -> int:
        return self.helper(0, n)

    def helper(self, low, high):
        if low >= high:
            return 1
        result = 0
        for i in range(low, high):
            left = self.helper(low, i)
            right = self.helper(i + 1, high)
            result += left * right
        return result


class Solution2:
    def numTrees(self, n):
        result = []
        result.append(1)
        for i in range(1, n + 1):
            temp = 0
            for j in range(i):
                j0 = i - j - 1
                temp += result[j] * result[j0]
            result.append(temp)
            print(result)
        return result[-1]


solution = Solution2()
print(solution.numTrees(4))
