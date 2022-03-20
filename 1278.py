class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        # 可以优化的hhhh
        def cost(l, r):
            count = 0

            while l <= r:
                if s[l] != s[r]:
                    count += 1
                l += 1
                r -= 1

            return count


        n = len(s)
        dp = [[float('+inf')] * (k + 1) for i in range(n)]

        for i in range(n):
            dp[i][1] = cost(0, i)
            # k == 1 的情况

        for i in range(n):
            for j in range(i):
                for p in range(2, k + 1):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost(j + 1, i))

                    # s[0] -> s[i] 分成p个组的最少cost

        return dp[-1][-1]





# 2022.3.11 我已不再是从前那个少年
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)

        cost = [[0] * n for i in range(n)]


        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    cost[i][j] = cost[i + 1][j - 1] + 1
                else:
                    cost[i][j] = cost[i + 1][j - 1]


        dp = [[float("+inf")] * (k + 1) for i in range(n)]
        # dp[i][j] s[0] -> s[i] 分割成 j 个组 需要修改的最少次数.


        for i in range(n):
            dp[i][1] = cost[0][i]

        for i in range(n):
            for j in range(i):
                for p in range(2, k + 1):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j + 1][i])

        return dp[-1][-1]


