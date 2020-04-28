# k=any
class Solution(object):
    def maxProfit(self, prices, k):
        length = len(prices)
        if k > length // 2:
            return self.maxProfit_any(prices)
        dp = [[0, 0] for _ in range(k + 1)]
        for i in range(k + 1):
            dp[i][0] = 0
            dp[i][1] = float('-inf')
        for i in range(length):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
        print(dp)
        return max([dp[i][0] for i in range(k + 1)])

    def maxProfit_any(self, prices):
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy:
                profit += prices[i] - buy
            buy = prices[i]
        return profit


solution = Solution()
a = [1, 3, 2, 8, 4, 9]
print(solution.maxProfit(a, 2))
