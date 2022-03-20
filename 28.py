# 遍历长度为len(needle)的所有字符串
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        l = len(needle)
        if l == 0: return 0
        for start in range(n - l + 1):
            if haystack[start : start + l] == needle:
                return start

        return -1


# 减少几次比较
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        l = len(needle)
        if l == 0: return 0
        for start in range(n - l + 1):
            if haystack[start] == needle[0]:
                cur_pos = start + 1
                i = 1
                while i < l:
                    if haystack[cur_pos] == needle[i]:
                        cur_pos += 1
                        i += 1
                    else:
                        break
                else:
                    return start
        return -1





# 大名鼎鼎的kmp算法
# next数组是当前位置的最长前后缀的长度
# 代码很工整，死背！！！

class Solution:
    def get_next(self, string, n):
        next = [0 for i in range(n)]
        j = 0
        for i in range(1, n):
            while j > 0 and string[i] != string[j]:
                j = next[j - 1]
            if string[i] == string[j]:
                j += 1

            next[i] = j

        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        m = len(haystack)
        n = len(needle)
        next = self.get_next(needle, n)

        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == n:
                return i - n + 1

        return -1
