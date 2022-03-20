# 枚举所有子序列 其实就是最长的有效子序列

from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        n = len(s)
        self.res = []
        self.max_len = 0
        def dfs(start, length, num_left, num_right, tmp):
            if num_left < num_right: return None

            if length > self.max_len and num_left == num_right:
                self.max_len = length
                self.res = []
                self.res.append(''.join(tmp[:]))

            elif num_left == num_right and length == self.max_len:
                self.res.append(''.join(tmp[:]))


            for i in range(start, n):
                if i > start and s[i] == s[i - 1]:
                    continue
                # 去重一下 也可以直接暴力哈希去重


                if s[i].isalpha():
                    tmp.append(s[i])
                    dfs(i + 1, length + 1, num_left, num_right, tmp)
                    tmp.pop()

                elif s[i] == ')':
                    tmp.append(s[i])
                    dfs(i + 1, length + 1, num_left, num_right + 1, tmp)
                    tmp.pop()

                elif s[i] == '(':
                    tmp.append(s[i])
                    dfs(i + 1, length + 1, num_left + 1, num_right, tmp)
                    tmp.pop()

        dfs(0, 0, 0, 0,[])
        return self.res



# 暴力枚举 BFS
class Solution:
    def removeInvalidParentheses(self, s:str) -> List[str]:
        def isValid(s:str)->bool:
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level


print(Solution().removeInvalidParentheses(")(f"))