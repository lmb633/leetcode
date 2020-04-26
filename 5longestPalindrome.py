# 动态规划
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ''
        length = len(s)
        dp = [[False, ] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
            if i > 0:
                dp[i][i - 1] = True
        for k in range(1, length):
            for i in range(length - k):
                if s[i] == s[i + k]:
                    dp[i][i + k] = dp[i + 1][i + k - 1]
        max_len = -1
        x, y = 0, 0
        for i in range(length):
            for j in range(i, length):
                if dp[i][j] and j - i > max_len:
                    max_len = j - i
                    x, y = i, j
        return s[x:y + 1]


# 中心扩散
class Solution2(object):
    def longestPalindrome(self, s):
        if not s:
            return ''
        x, y = 0, 0
        max_len = 1
        length = len(s)
        for c in range(length - 1):
            i, j = c, c
            while i >= 0 and j < length:
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            if j - i - 1 > max_len:
                max_len = j - i - 1
                x, y = i + 1, j - 1
            if s[c] == s[c + 1]:
                i, j = c, c + 1
                while i >= 0 and j < length:
                    if s[i] != s[j]:
                        break
                    i -= 1
                    j += 1
                if j - i - 1 > max_len:
                    max_len = j - i - 1
                    x, y = i + 1, j - 1
        return s[x:y + 1]
