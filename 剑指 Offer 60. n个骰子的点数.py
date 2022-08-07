from typing import List
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        # 最直接的dp
        dp = [[0] * (6 * n + 1) for i in range(n + 1)]

        for j in range(1, 7):
            dp[1][j] = 1

        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for k in range(1, 7):
                    if j - k >= i - 1:
                        # 因为仍i - 1个骰子，最少出现的点数和为i - 1
                        dp[i][j] += dp[i - 1][j - k]

        res = []
        for j in range(n, 6 * n + 1):
            res.append(dp[n][j] / 6 ** n)

        return res

# 节省空间
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [0] * (6 * n + 1)

        for i in range(1, 7):
            dp[i] = 1

        for i in range(2, n + 1):
            for j in range(6 * i, i - 1, -1):
                dp[j] = 0
                for k in range(1, 7):
                    if j - k >= i - 1:
                        dp[j] += dp[j - k]

        res = []
        for i in range(n, 6 * n + 1):
            res.append(dp[i] / 6 ** n)

        return res

