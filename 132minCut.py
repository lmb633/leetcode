class Solution(object):
    def minCut(self, s):
        if not s or len(s) < 2:
            return 0
        length = len(s)
        is_p = [[False, ] * length for _ in range(length)]
        for i in range(length):
            is_p[i][i] = True
            if i > 0:
                is_p[i][i - 1] = True
        for k in range(1, length):
            for i in range(length - k):
                if s[i] == s[i + k]:
                    is_p[i][i + k] = is_p[i + 1][i + k - 1]

        dp = [0] * (length + 1)
        dp[0] = -1
        for i in range(1, length):
            min_cut = i
            for j in range(i + 1):
                if is_p[j][i] is True:
                    temp = dp[j]
                    if temp + 1 < min_cut:
                        min_cut = temp + 1
            dp[i + 1] = min_cut
        return dp[-1]
