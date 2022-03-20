class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(None)
        def dfs(index, tmp):
            if tmp == amount:
                return 1

            res = 0
            for i in range(index, n):
                if tmp + coins[i] <= amount:
                    res += dfs(i, tmp + coins[i])

            return res

        return dfs(0, 0)





class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0 for i in range(amount + 1)]
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i - coin]

        return dp[-1]


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [[0] * (amount + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        # 前0个凑j dp[0][j] 很显然是0 所以不用初始化
        # 所以下面循环只需要(1, n + 1) (1, amount + 1)

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                val_this = coins[i - 1]
                if j - val_this >= 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - val_this]
                else:
                    dp[i][j] = dp[i - 1][j]

        print(dp)

        return dp[-1][-1]

