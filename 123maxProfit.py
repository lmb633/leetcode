# k=2
class Solution(object):
    def maxProfit(self, prices, k):
        length = len(prices)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(length + 1)]
        for i in range(length + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = float('-inf')
        for i in range(length):
            for j in range(k, 0, -1):
                dp[i + 1][j][0] = max(dp[i][j][0], dp[i][j][1] + prices[i])
                dp[i + 1][j][1] = max(dp[i][j][1], dp[i][j - 1][0] - prices[i])
        print(dp)
        return max([dp[-1][i][0] for i in range(k + 1)])


solution = Solution()
a = [1, 2, 3, 4, 5]
print(solution.maxProfit(a, 2))
