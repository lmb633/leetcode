class Solution(object):
    def change(self, amount, coins):
        num = len(coins)
        result = [[0] * (amount + 1) for _ in range(num + 1)]
        for i in range(num + 1):
            result[i][0] = 1
        # for i in range(amount+1):
        #     result[0][i]=1
        for i in range(1, num + 1):
            coin = coins[i - 1]
            for j in range(1, amount + 1):
                if j - coin >= 0:
                    result[i][j] = result[i][j - coin] + result[i - 1][j]
                else:
                    result[i][j] = result[i - 1][j]
        # print(result)
        return result[-1][-1]
