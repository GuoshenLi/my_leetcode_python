# 卖股票收费
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:


        # 一种状态就是在一天交易结束之后有股票
        # 另一种状态就是一天交易结束之后没有股票
        n = len(prices)
        dp = [[0, 0] for _ in range(len(prices))]
        # 状态0没有股票
        dp[0][0] = 0
        # 状态1 有股票 (买股票)所以减号
        dp[0][1] = -prices[0]
        # 卖股票 加号

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

        # 最后一天交易结束不持有股票的利润肯定要比持有股票的利润要来的大
        # 因为如果持有股票肯定要用钱去买，因此会对降低利润
        return dp[n-1][0]
        # 当然想不通的话也可以 max(dp[n - 1][0], dp[n - 1][1])

# 买股票收费 也一样的


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:


        # 一种状态就是在一天交易结束之后有股票
        # 另一种状态就是一天交易结束之后没有股票
        n = len(prices)
        dp = [[0, 0] for _ in range(len(prices))]
        # 状态0没有股票
        dp[0][0] = 0
        # 状态1 有股票 (买股票)所以减号 注意因为买股票收费 所以要在这里"-fee"
        dp[0][1] = -prices[0] - fee
        # 卖股票 加号

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)


        return dp[n-1][0]

