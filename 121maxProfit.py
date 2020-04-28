class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        stack = []
        i = 0
        while i < len(prices):
            while stack and stack[-1] >= prices[i]:
                if max_profit < stack[-1] - stack[0]:
                    max_profit = stack[-1] - stack[0]
                stack.pop()
            stack.append(prices[i])
            i += 1
        if stack and max_profit < stack[-1] - stack[0]:
            max_profit = stack[-1] - stack[0]
        return max_profit


class Solution2(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                temp = prices[i] - buy
                if temp > profit:
                    profit = temp
        return profit


# 状态机
class Solution3(object):
    def maxProfit(self, prices):
        length = len(prices)
        dp = [[0, 0] for i in range(length + 1)]
        print(dp)
        dp[0][0] = 0
        dp[0][1] = float('-inf')
        for i in range(length):
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i])
            dp[i + 1][1] = max(dp[i][1], -prices[i])
        print(dp)
        return dp[-1][0]


solution = Solution3()
a = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(a))
