from typing import List
# 记忆化递归 第一次自己写出来 3.7
# memo存储的是节点为i的时候的往下扩张的最小值（若能扩张），若不能扩张则为-1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        @lru_cache(None)
        def dfs(tmp):
            if tmp == amount: return 0
            res = float('+inf')

            for i in range(n):
                if tmp + coins[i] <= amount:
                    step = dfs(tmp + coins[i])
                    if step != -1:
                        res = min(res, step + 1)

            return -1 if res == float('+inf') else res

        return dfs(0)



# dp数组存amount为i的时候的最小兑换次数。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('+inf')] * (1 + amount) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0
        # 仔细想一下这个初始化

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                val_this = coins[i - 1]
                if j - val_this >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - val_this] + 1)
                                                 # 下标i 因为可以重复
                                                 # 0-1背包从i - 1
                else:
                    dp[i][j] = dp[i - 1][j]

        return -1 if dp[-1][-1] == float('+inf') else dp[-1][-1]





# dp数组存amount为i的时候的最小兑换次数。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('+inf') for i in range(amount + 1)]
        dp[0] = 0

        for coin in coins:
            for i in range(1, amount + 1):

                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == float('+inf') else dp[-1]