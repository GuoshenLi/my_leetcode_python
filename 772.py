from collections import deque
class Solution:
    def calculate(self, s: str) -> int:

        queue = deque(s)
        return self.helper(queue)

    def helper(self, s):

        stack = []
        num = 0
        pre_sign = '+'

        while s:
            char = s.popleft()

            if char.isdigit():
                num = num * 10 + int(char)

            if char == '(':
                num = self.helper(s)

            if not char.isdigit() and char != ' ' or len(s) == 0:
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                elif pre_sign == '/':
                    stack.append(int(stack.pop() / num))

                pre_sign = char
                num = 0

            if char == ')':
                break

        return sum(stack)