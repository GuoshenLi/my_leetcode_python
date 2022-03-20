from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for k, v in t_count.items():
            if k not in s_count or v != s_count[k]:
                return k

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = [0 for _ in range(26)]

        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            s_count[ord(t[i]) - ord('a')] -= 1
            if s_count[ord(t[i]) - ord('a')] < 0:
                return t[i]


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 异或
        res = 0

        for char in s:
            res = res ^ ord(char)

        for char in t:
            res = res ^ ord(char)

        return chr(res)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 异或
        res_s = 0
        res_t = 0
        for char in s:
            res_s += ord(char)

        for char in t:
            res_t += ord(char)

        return chr(res_t - res_s)



