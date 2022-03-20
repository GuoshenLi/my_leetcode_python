class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        memo = [[None] * n for _ in range(m)]
        # 最长公共子序列！
        # 与最长回文子序列516！基本一样！
        def dfs(i, j):
            if i == m or j == n:
                return 0

            if memo[i][j] != None:
                return memo[i][j]

            if word1[i] == word2[j]:
                memo[i][j] = 1 + dfs(i + 1, j + 1)
                return memo[i][j]

            else:
                memo[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
                return memo[i][j]

        return m + n - 2 * dfs(0, 0)