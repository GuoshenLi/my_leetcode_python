from collections import deque
#与227一样

class Solution:
    def calculate(self, s: str) -> int:
        s = deque(s)
        return self.helper(s)

    # 递归helper其实就是算每个相应括号内的值（一层一层拨开）背几遍代码
    def helper(self, s):

        stack = []
        sign = '+'
        num = 0

        while len(s) > 0:
            c = s.popleft()
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num

            if c == '(':
                num = self.helper(s)
            # if c in '+-*/()' or len(s) == 0: we need to include ) the 右括号 here!

            if not c.isdigit() and c != ' ' or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)


                num = 0
                sign = c

            if c == ')': break

        return sum(stack)



print(Solution().calculate_(s = "(1 + 2) + (3 - (6 + 4))"))