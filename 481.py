# 找到生成字符串的规律


class Solution:
    def magicalString(self, n: int) -> int:

        s = "122"
        i = 2

        while len(s) < n:
            if s[-1] == '2':
                s += '1' * int(s[i])
                i += 1
            else:
                s += '2' * int(s[i])
                i += 1

        return s[:n].count('1')

