# 贪心算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i] - prices[i-1]

        return ans

# 股票题 背动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp动态规划

        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = - prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]
