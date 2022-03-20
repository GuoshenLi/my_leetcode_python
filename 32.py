# 暴力法 220 / 231
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):

                if self.is_valid(s[i: j + 1], j - i + 1):
                    ans = max(ans, j - i + 1)

        return ans

    def is_valid(self, str_, length):
        stack = []

        for i in range(length):
            if str_[i] == '(':
                stack.append('(')
            else: # ')'
                if not stack or stack[-1] == ')':
                    return False
                else:
                    stack.pop()
        return not stack


# 动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0

        # 因为dp[0] 下标为0的话因为是奇数个所以不可能匹配。

        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2

                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)

        return max(dp)


# 常规做法 利用栈
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        # 让栈不为空
        res = 0
        for i in range(len(s)):
            top_index = stack[-1]

            if top_index != -1 and s[i] == ')' and s[top_index] == '(':
                                                # 为了保证不出错 top_index 要判断不等于 -1
                stack.pop()
                res = max(res, i - stack[-1])

            else:
                stack.append(i)

        return res


solu = Solution()
print(solu.longestValidParentheses(s = '()(())'))