# 股票题 看动态规划

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 只能进行一笔交易
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0 # 卖
        dp[0][1] = -prices[0] # 买

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])


        return max(dp[n - 1][0], dp[n - 1][1])


# IT5001 期末考 竟然可以用分治
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0

        mid = len(prices) // 2
        left = prices[:mid]
        right = prices[mid:]
        return max(self.maxProfit(left),
                   self.maxProfit(right),
                   max(right) - min(left))




# 暴力解法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(prices[j] - prices[i], max_profit)
        return max_profit

# 遍历一遍 O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            if p - min_price > max_profit:
                max_profit = p - min_price

        return max_profit

# 单调栈
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        prices += [0]
        max_profit = 0
        for i in range(len(prices)):
            while stack and prices[i] <= stack[-1]:
                max_profit = max(max_profit, stack[-1] - stack[0])
                stack.pop()

            stack.append(prices[i])

        return max_profit









