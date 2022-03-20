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
        # 生成过程中左括号的数量 >= 右括号的数量
        res = []
        def dfs(index, num_left, num_right, tmp):
            if num_left < num_right: return None
            if index == 2 * n:
                if num_left == n and num_right == n:
                    res.append(''.join(tmp))
                return None



            tmp.append('(')
            dfs(index + 1, num_left + 1, num_right, tmp)
            tmp.pop()

            tmp.append(')')
            dfs(index + 1, num_left, num_right + 1, tmp)
            tmp.pop()



        dfs(0, 0, 0, [])
        return res


print(Solution().generateParenthesis(n = 1))