class Solution2(object):
    def maxProfit(self, prices):
        length = len(prices)
        dp = [[0, 0] for i in range(length + 2)]
        print(dp)
        dp[0][1] = float('-inf')
        dp[1][1] = float('-inf')
        for i in range(length):
            dp[i + 2][0] = max(dp[i+1][0], dp[i+1][1] + prices[i])
            dp[i + 2][1] = max(dp[i+1][1], dp[i][0] - prices[i])
        return dp[-1][0]