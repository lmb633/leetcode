class Solution(object):
    # 状态转移
    def maxProfit(self, prices, fee):
        length = len(prices)
        sale = 0
        buy = float('-inf')
        for i in range(length):
            print(sale,buy)
            temp = sale
            sale = max(sale, buy + prices[i])
            buy = max(buy, temp - prices[i] - fee)
            # print(sale, buy)
        return sale

    # 贪心法
    def maxProfit2(self, prices, fee):
        length = len(prices)
        profit = 0
        buy_in = prices[0]
        temp = 0
        for i in range(1, length):
            # print(buy_in, prices[i], temp, profit)
            if prices[i] < buy_in or prices[i] + fee <= buy_in + temp:
                buy_in = prices[i]
                if temp - fee > 0:
                    profit += temp - fee
                temp = 0
            else:
                if prices[i] - buy_in > temp:
                    temp = prices[i] - buy_in
        if temp - fee > 0:
            profit += temp - fee
        return profit


solution = Solution()
a = [2, 2, 1, 1, 5, 5, 3, 1, 5, 4]
print(solution.maxProfit(a, 2))
print(solution.maxProfit2(a, 2))
