class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0, 0, 0] for _ in range(n)]

        # dp[i][0] , 持有股票
        # dp[i][1] , 不持有股票，不处于冷冻期
        # dp[i][2] , 不持有股票，处于冷冻期

        dp[0][0] = -prices[0]
        # 对第一天买入的状态初始化
        # 从第二天开始迭代
        #
        for i in range(1, n):
            # 第i天持有股票的最大收益，等价于第i - 1天持有股票的收益与第i - 1天不持有股票，不处于冷冻期再在今天买的利润的最大值
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2]) # 前一天处于冷冻期，今天就不处于了
            dp[i][2] = dp[i - 1][0] + prices[i] # 只有这一种情况，前一天不持有股票，不处于冷冻期，再在今天买

        return max(dp[n - 1][1], dp[n - 1][2])



