from collections import deque
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = deque([
            ["", 0, 0]
        ])
        final = []

        while results:
            str_, left_brackets, right_brackets = results.popleft()

            if left_brackets + right_brackets == 2 * n:
                if left_brackets == right_brackets:
                    final.append(str_)
                continue
            # left brackets 只可能大于或等于 right brackets
            if left_brackets > right_brackets:
                results.append([str_ + ")", left_brackets, right_brackets + 1])
            results.append([str_ + "(", left_brackets + 1, right_brackets])

        return final



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 记录左右括号个数的差值  #left - #right 应该 >= 0才可以。

        res = []

        def dfs(tmp, index, num_left, num_right):
            if index > n * 2: return None
            elif num_left < num_right: return None
            elif num_left > n or num_right > n: return None
            elif num_left == num_right == n:
                res.append(''.join(tmp))
                return None

            for i in ['(', ')']:
                tmp.append(i)
                if i == '(':
                    dfs(tmp, index + 1, num_left + 1, num_right)
                elif i == ')':
                    dfs(tmp, index + 1, num_left, num_right + 1)

                tmp.pop()

        dfs([], 0, 0, 0)

        return res

print(Solution().generateParenthesis(n = 1))