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


solution = Solution()
a = [7, 1]
print(solution.maxProfit(a))
