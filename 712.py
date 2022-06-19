# 记忆化递归 动态规划
# 可以转换为 最长公共子序列
# ASCII 码最大的公共子序列
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        m_sum = sum(ord(char) for char in s1)
        n_sum = sum(ord(char) for char in s2)

        memo = {}

        def dfs(i, j):
            if i == m or j == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s1[i] == s2[j]:
                memo[(i, j)] = ord(s1[i]) + dfs(i + 1, j + 1)
                return memo[(i, j)]

            else:
                memo[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
                return memo[(i, j)]

        return m_sum + n_sum - 2 * dfs(0, 0)




class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # ASCII码最大的公共子序列
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return sum(ord(char) for char in s1) + sum(ord(char) for char in s2) - 2 * dp[-1][-1]