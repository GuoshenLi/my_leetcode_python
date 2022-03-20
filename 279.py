# 动态规划
import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('+inf') for i in range(n + 1)]

        dp[0] = 0
        perfect_square_pool = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]


        # 背包问题nums数组要放外面
        for num in perfect_square_pool:
            for i in range(1, n + 1):
                if i - num >= 0:
                    dp[i] = min(dp[i - num] + 1, dp[i])


        return dp[-1]



import math
class Solution:
    def numSquares(self, n: int) -> int:

        square = []

        for i in range(1, int(math.sqrt(n)) + 1):
            square.append(i ** 2)
        length = len(square)
        # 这是一个完全背包问题

        dp = [[float('+inf')] * (n + 1) for i in range(length + 1)]

        for i in range(length + 1):
            dp[i][0] = 0

        for i in range(1, length + 1):
            weight = square[i - 1]
            for j in range(1, n + 1):
                if j - weight >= 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - weight] + 1)
                else:
                    dp[i][j] = dp[i - 1][j]


        return dp[-1][-1]




import math
class Solution:
    def numSquares(self, n: int) -> int:


        square = []

        for i in range(1, int(math.sqrt(n)) + 1):
            square.append(i ** 2)

        length = len(square)

        @lru_cache(None)
        def dfs(tmp):
            if tmp == n: return 0
            if tmp > n: return -1

            res = float('inf')
            for i in range(length):
                tmp_res = dfs(tmp + square[i])
                if tmp_res != -1:
                    res = min(res, tmp_res + 1)

            return -1 if res == float('+inf') else res

        return dfs(0)





print(Solution().numSquares(n = 11))