class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        #--------------- 先找最长公共子序列LCS -----------------#
        dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
        LCS = dp[m][n]

        #--------------------- 从前往后添加
        res = ""
        i = 0
        j = 0
        for c in LCS:
            while i < m and str1[i] != c:
                res += str1[i]
                i += 1
            while j < n and str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1

        res += str1[i: ]
        res += str2[j: ]
        return res
