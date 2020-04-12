import math


class Solution:
    def numSquares(self, n):
        sqr_num = [i ** 2 for i in range(int(math.sqrt(n) + 1))]
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            temp = n
            j = 1
            while j < len(sqr_num) and sqr_num[j] <= i:
                if result[i - sqr_num[j]] + 1 < temp:
                    temp = result[i - sqr_num[j]] + 1
                j += 1

            result[i] = temp
        return result[-1]
