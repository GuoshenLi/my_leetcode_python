class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        match = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in match:  # 左括号
                stack.append(char)

            else:  # 看栈顶匹配与否
                if stack and match[stack[-1]] == char:
                    stack.pop()

                else:  # 不匹配
                    return False

        if not stack:
            return True
        else:
            return False
