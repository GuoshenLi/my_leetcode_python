class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for i in range(m + 1)]

        dp[0][0] = True
        # for j in range(2, n + 1):
        #         dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'


        for j in range(2, n + 1):
            if j % 2 == 0:
                if p[j - 1] == '*':
                    dp[0][j] = True
                else:
                    break


        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or self.first_match(s, p, i - 1, j - 2) and dp[i - 1][j]
                    # s = aacd     p = a*cd
                    # i == j == 4
                    # dp[i][j - 2] 压根不用a*
                    # 用一个或多个 i - 1 与 j - 2 要匹配。若成功，相当
                    # 于删掉一个a，再i - 1与j匹配
                    # 仔细理解这个代码！！！

                else:
                    dp[i][j] = self.first_match(s, p, i - 1, j - 1) and dp[i - 1][j - 1]


        return dp[m][n]



    def first_match(self, s, p, i, j):
        if s[i] == p[j] or p[j] == '.':
            return True
        else:
            return False

Solution().isMatch(s = "aab",p = "c*a*b")


