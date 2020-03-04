#最长重复子数组
class Solution(object):
    def findLength(self, A, B):
        dp=[[0 for i in range(len(A))] for j in range(len(B))]
        for i in range(len(B)):
            for j in range(len(A)):
                if B[i]==A[j]:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=0
        return max([max(col) for col in dp])

