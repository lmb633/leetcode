class Solution(object):
    def coinChange(self, coins, amount):
        coins = set(coins)
        result = [0] * (amount + 1)
        for i in range(1, amount + 1):
            temp_min = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    temp = result[i - coin] + 1
                    if temp < temp_min:
                        temp_min = temp
            result[i] = temp_min
        return result[-1] if result[-1] != float('inf') else -1

        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
