# 暴力解法 python不通过
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        length = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_Palindrome(s, i, j):
                    if j - i + 1 > length:
                        length = j - i + 1
                        start = i

        return s[start:start + length]

    def is_Palindrome(self, s, left, right):
        while right >= left:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


# 中心扩散
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]



# 统一顺序打表 和最长回文子序列 最长回文子串 以及 分割字符串
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[True] * n for i in range(n)]

        length = 1
        left = 0

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and j - i + 1 > length:
                    left = i
                    length = j - i + 1

        return s[left: left + length]