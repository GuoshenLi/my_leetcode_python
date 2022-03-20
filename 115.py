# 枚举所有子序列 暴力
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if s == t: return 1
        m = len(s)
        n = len(t)

        def dfs(index, tmp):
            if n == len(tmp):
                return int(''.join(tmp) == t)
            res = 0
            for i in range(index, m):
                tmp.append(s[i])
                res += dfs(i + 1, tmp)
                tmp.pop()

            return res

        return dfs(0, [])



s = Solution()
print(s.numDistinct(s = "rabbbit", t = "rabbit"))



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for i in range(m + 1)]
        # t的空字符串在s出现的次数为1
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]


        return dp[-1][-1]