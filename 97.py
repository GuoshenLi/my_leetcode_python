# 记忆化递归
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        if len_s1 + len_s2 != len_s3: return False
        memo = {}

        def dfs(i, j, k):
            if (i, j, k) in memo: return memo[(i, j, k)]
            if k == len_s3: return True
            is_valid = False

            if i < len_s1 and s1[i] == s3[k]:
                choce1 = dfs(i + 1, j, k + 1)
                is_valid |= choce1

            if j < len_s2 and s2[j] == s3[k]:
                choce2 = dfs(i, j + 1, k + 1)
                is_valid |= choce2

            memo[(i, j, k)] = is_valid
            if is_valid:
                return True
            else:
                return False

        return dfs(0, 0, 0)








class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)

        if len_s1 + len_s2 != len_s3: return False

        # dp[i][j] 表示什么？ s1的前i个字符 与s2的前j个字符 能够构成s3
        # 的前i + j个字符。

        dp = [[False] * (len_s2 + 1) for i in range(len_s1 + 1)]

        dp[0][0] = True

        for i in range(1, len_s1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break

        for j in range(1, len_s2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break


        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                # 注意下标 s3[i + j - 1]
                # s1[i - 1] s2[j - 1]

                # 考虑s3的最后一个字符s3[i+j-1]来自哪里？做状态转移：
                # 1）如果来自s1[i-1]，则dp[i][j] 为：s1前缀长度i-1 + s2前缀长度j 能否交错组成s3前缀长度i+j-1，即：dp[i-1][j]
                # 2）如果来自s2[j-1]，则dp[i][j] 为：s1前缀长度i + s2前缀长度j-1 能否交错组成s3前缀长度i+j-1，即：dp[i][j-1]

                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]

                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]


        return dp[len_s1][len_s2]