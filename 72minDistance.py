class Solution(object):
    def minDistance(self, word1, word2):
        if word1 is None or word2 is None:
            return None
        len1 = len(word1)
        len2 = len(word2)
        dp = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
        for i in range(len1 + 1):
            dp[0][i] = i
        for i in range(len2 + 1):
            dp[i][0] = i

        for i in range(1, len2 + 1):
            for j in range(1, len1 + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] - 1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        # print(dp)
        return dp[-1][-1]

        """
        :type word1: str
        :type word2: str
        :rtype: int
        """