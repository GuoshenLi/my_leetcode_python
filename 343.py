# 典型的记忆化搜索
class Solution:
    def integerBreak(self, n: int) -> int:

        memo = [None] * (n + 1)
        def dfs(n):
            if n == 1:
                return 0
            if memo[n]:
                return memo[n]

            res = float('-inf')
            for i in range(1, n):
                res = max(res, i * (n - i), i * dfs(n - i))

            memo[n] = res
            return memo[n]

        return dfs(n)


print(Solution().integerBreak(n = 24))


class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                #                 只能拆两个       还可以继续拆分
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
                # dp[i] = max(dp[i], j * (i - j), (i - j) * dp[j])
        return dp[n]

