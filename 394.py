# 阿里云面试题目


class Solution:

    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif c.isdigit():
                multi = multi * 10 + int(c)
            else:
                res += c
        return res


# 用队列做 跟计算器一摸一样基本

from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:

        s = deque(s)
        return self.helper(s)


    def helper(self, s):
        res = ""
        num = 0

        while len(s) > 0:
            char = s.popleft()
            if char.isdigit():
                num = num * 10 + int(char)

            if char == '[':
                res += num * self.helper(s)
                num = 0

            if char.isalpha():
                res += char

            if char == ']':
                break

        return res








# 困难
class Solution:
    def decodeString(self, s: str) -> str:
        m = len(s)

        def dfs(index):
            res, multiple = '', 0
            while index < m:

                if s[index].isdigit():
                    multiple = multiple * 10 + int(s[index])

                elif s[index] == '[':
                    sub, index = dfs(index + 1)
                    res += multiple * sub
                    multiple = 0

                elif s[index] == ']':
                    return res, index

                else:
                    res += s[index]

                index += 1

            return res

        return dfs(0)



print(Solution().decodeString("3[a]2[bc]"))