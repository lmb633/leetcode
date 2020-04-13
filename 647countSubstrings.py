class Solution(object):
    def countSubstrings(self, s):
        length = len(s)
        if length < 1:
            return 0
        dp = [[0] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for k in range(1, length):
            for i in range(length - k):
                if s[i] == s[i + k]:
                    if k == 1:
                        dp[i][i + k] = 1
                    else:
                        dp[i][i + k] = dp[i + 1][i + k - 1]
                else:
                    dp[i][i + k] = 0
        # print(dp)
        result = 0
        for l in dp:
            result += sum(l)
        return result
