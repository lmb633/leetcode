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


solution = Solution()
a = [7,1]
print(solution.maxProfit(a))
