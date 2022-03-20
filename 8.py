class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        i = 0
        flag = '+'
        nums = 0
        if s[i] == '-':
            flag = '-'
            i += 1

        elif s[i] == '+':
            # 为了代码对称 再多加一行flag = '+'
            flag = '+'
            i += 1


        for i in range(i, len(s)):
            if not s[i].isdigit():
                break
            nums = 10 * nums + int(s[i])
            if flag == '+' and nums > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif flag == '-' and -nums < - 2 ** 31:
                return -2 ** 31

        if flag == '+':
            return nums
        else:
            return - nums