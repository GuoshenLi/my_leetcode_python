# 一气呵成的递归 超时
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        self.res = 0
        length = len(s)

        def dfs(start, tmp):
            self.res = max(self.res, self.cal_length(''.join(tmp)))

            for end in range(start, length):
                tmp.append(s[end])
                dfs(end + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return self.res

    def cal_length(self, string):
        left = 0
        right = len(string) - 1

        while left < right:
            if string[left] != string[right]:
                flag = False
                break
            left += 1
            right -= 1
        else:
            flag = True

        return len(string) if flag == True else 0

# 难点在于如何定义递归子问题
# 解决重叠子问题的递归做法！！！
# 和586最长公共子序列一样！！！！
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # base case
            if i > j:
                return 0
            if i == j:
                return 1
            # 状态转移方程
            if s[i] == s[j]:
                memo[(i, j)] = dp(i + 1, j - 1) + 2
            else:
                memo[(i, j)] = max(dp(i + 1, j), dp(i, j - 1))
            return memo[(i, j)]

        memo = dict()  # 存储 （i，j）的信息
        return dp(0, len(s) - 1)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2

                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]