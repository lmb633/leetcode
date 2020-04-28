# 贪心算法
class Solution(object):
    def maxProfit(self, prices):

        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += prices[i] - buy
            buy = prices[i]
        return profit


# 动态规划
class Solution2(object):
    def maxProfit(self, prices):
        length = len(prices)
        dp = [[0, 0] for i in range(length + 1)]
        print(dp)
        dp[0][0] = 0
        dp[0][1] = float('-inf')
        for i in range(length):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i])
        return dp[-1][0]
