class Solution(object):
    def waysToChange(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in [1, 5, 10, 25]:
            for i in range(1, n + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]
            print(dp)

        return dp[-1]
