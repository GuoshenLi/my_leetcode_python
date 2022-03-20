# 这题目是最长公共子串
# 最长公共子序列

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        # dp[i][j] 储存的是 A中的前i个字符与B中的前j个字符的最长公共子串
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # m行 n列


        max_ = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_ = max(max_, dp[i][j])


        return max_