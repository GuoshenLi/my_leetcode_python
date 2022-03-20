import tensorflow as tf
# 392 双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        len_s = len(s)
        len_t = len(t)

        i = 0
        j = 0

        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1

            j += 1

        return i == len_s


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m = len(s)
        n = len(t)
        dp = [[False] * (n + 1) for i in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[m][n]



