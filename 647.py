# 中心扩散 和第五题一样
class Solution:
    def countSubstrings(self, s: str) -> int:

        result = 0
        length = len(s)
        for i in range(length):

            result += (self.palindromic_substring(s, i, i)
            + self.palindromic_substring(s, i, i + 1))

        return result



    def palindromic_substring(self, s, left, right):
        res = 0
        while right < len(s) and left >= 0 and s[left] == s[right]:
            res += 1
            right += 1
            left -= 1

        return res





class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[True] * n for i in range(n)]
        res = 0

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] == True: res += 1

        return res + n
