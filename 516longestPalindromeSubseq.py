class Solution(object):
    def longestPalindromeSubseq(self, s):
        length = len(s)
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for k in range(1, length):
            for i in range(length - k):
                if s[i] == s[i + k]:
                    dp[i][i + k] = dp[i + 1][i + k - 1] + 2
                else:
                    dp[i][i + k] = max(dp[i + 1][i + k], dp[i][i + k - 1])
        print(dp)
        return dp[0][length - 1]

        """
        :type s: str
        :rtype: int
        """
