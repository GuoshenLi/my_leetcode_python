class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)

        # 0: 啥都不干
        # 1: 买入1次
        # 2: 卖出1次
        # 3: 买入2次
        # 4: 卖出2次
        # ...
        # 2k - 1: 买入k次
        # 2k: 卖出k次

        dp = [[0 for _ in range(2 * k + 1)] for _ in range(n)]
        # 初始化第0天
        for i in range(1, 2 * k + 1, 2): # 注意range（开始，结束，递增多少）
            dp[0][i] = -prices[0]

        # 因为已经初始化第0天，所以从第一天开始
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            for j in range(1, 2 * k + 1):
                if j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]+ prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]- prices[i])

        return dp[n - 1][2 * k]


