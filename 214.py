# 暴力法 119 / 120
class Solution:
    def is_palindrome(self, string):
        n = len(string)
        left, right = 0, n - 1
        while left < right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True


    def shortestPalindrome(self, s: str) -> str:
        # 右边去掉0个字符，去掉1个字符，去掉2个字符，...，去掉n - 1个字符
        # 判断是否回文，如果回文，则把去掉的那一段反一下加到s的前面即可。
        if not s: return ''
        n = len(s)
        for i in range(n):
            if self.is_palindrome(s[:n - i]):
                return s[n - i:][::-1] + s


# 119 / 200
# 其实整个题目就是求从s[0]开始的最长回文串
# 然后把后面不回文的部分倒过来加到s开头即可

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s: return s
        n = len(s)
        dp = [[True] * n for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])


        for j in range(n - 1, -1, -1):
            if dp[0][j] == True:
                return s[j + 1:][::-1] + s




# 可以套用kmp算法求next数组那个，太牛逼了。
class Solution:
    # 很巧妙啊 其实就是kmp求next数组
    def shortestPalindrome(self, s: str) -> str:
        if not s: return s
        # s: abab (aba)b
        # s + '#' + s[::-1] == (aba)b # b(aba)
        # 其实就是求这个的最长公共前后缀。

        next = self.get_next(s + '#' + s[::-1])

        max_len = next[-1]

        return s[max_len:][::-1] + s


    def get_next(self, s):
        n = len(s)
        next = [0 for i in range(n)]

        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1

            next[i] = j

        return next





class Solution:
    def get_next(self, s):
        n = len(s)
        next = [0 for i in range(n)]
        # 求最长公共前后缀不能include 第一个或者最后一个字符
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1

            next[i] = j

        return next


print(Solution().get_next(s = "aacecaaa"))


