class Solution(object):
    def findTargetSumWays(self, nums, S):
        length = len(nums)
        if S < 0:
            S = -S
        sum_ = sum(nums)
        if S > sum_:
            return 0
        dp = [[0] * (sum_ + 1) for _ in range(length + 1)]
        dp[0][0] = 1
        for i in range(1, length + 1):
            for j in range(0, sum_ + 1):
                if j + nums[i - 1] <= sum_:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] += dp[i - 1][nums[i - 1] - j]
        return dp[length][S]
