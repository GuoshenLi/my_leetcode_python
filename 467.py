class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # 重复的子串不计数
        dp = [0] * 26
        # dp[i] 26个字母当中以第i个字母为末尾的 连续子串的最大长度
        # 例子 "abcdabc"
        dp[ord(p[0]) - ord('a')] += 1
        max_len = 1
        # max_len 记录截至目前为止 连续的字符最大长度
        n = len(p)
        for i in range(1, n):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                max_len += 1

            else:
                max_len = 1
            dp[ord(p[i]) - ord('a')] = max(dp[ord(p[i]) - ord('a')], max_len)
        return sum(dp)




# 暴力法 只能过12 / 81
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        table = set()

        for i in range(n):
            for j in range(i, n):
                if self.is_valid(p[i:j + 1], j - i + 1):
                    table.add(p[i:j + 1])

        return len(table)

    def is_valid(self, s, length):
        pointer = 1
        while pointer < length:
            if (ord(s[pointer]) - ord(s[pointer - 1])) % 26 == 1:
                pointer += 1
            else:
                return False

        return True

