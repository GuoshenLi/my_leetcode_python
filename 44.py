class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 两种情况
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                    # j可以匹配多个所以j指针保持不动
                else:
                    dp[i][j] = self.first_match(s, p, i - 1, j - 1) and dp[i - 1][j - 1]
                    # 与第10题一样的写法
        return dp[m][n]

    def first_match(self, s, p, i, j):
        if s[i] == p[j] or p[j] == '?':
            return True
        else:
            return False