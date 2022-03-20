from typing import List
# 要反推 记忆化递归
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        # 从i, j出发到公主至少要多少血量
        memo = [[None] * n for i in range(m)]

        def dfs(i, j):

            if i == m - 1 and j == n - 1:
                if dungeon[-1][-1] > 0:
                    return 1
                else:
                    return 1 - dungeon[-1][-1]

            if memo[i][j]: return memo[i][j]

            if i == m - 1:  # 在最后一行
                memo[i][j] = max(dfs(i, j + 1) - dungeon[i][j], 1)
                return memo[i][j]

            if j == n - 1:  # 在最后一列
                memo[i][j] = max(dfs(i + 1, j) - dungeon[i][j], 1)
                return memo[i][j]

            memo[i][j] = max(min(dfs(i + 1, j), dfs(i, j + 1)) - dungeon[i][j], 1)
            return memo[i][j]

        return dfs(0, 0)


print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = [[float('inf')] * n for i in range(m)]

        dp[-1][-1] = 1 if dungeon[-1][-1] > 0 else 1 - dungeon[-1][-1]
        # 因为最少要留一滴血 因此的话 一定要max(1, xxx)
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]

