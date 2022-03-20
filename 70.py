class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def dfs(tmp):
            if tmp == n: return 1
            if tmp  > n: return 0

            res = 0
            for i in range(1, 3):
                res += dfs(tmp + i)

            return res

        return dfs(0)



class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            for step in [1, 2]:
                if i - step >= 0:
                    dp[i] += dp[i - step]

        return dp[-1]
