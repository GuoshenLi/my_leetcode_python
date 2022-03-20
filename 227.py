from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        s = deque(s)
        stack = []
        num = 0
        presign = '+'

        while len(s) > 0:
            char = s.popleft()

            if char.isdigit():
                num = num * 10 + int(char)

            if not char.isdigit() and char != ' ' or len(s) == 0:
                if presign == '+': stack.append(num)
                elif presign == '-': stack.append(-num)
                elif presign == '*': stack.append(stack.pop() * num)
                elif presign == '/': stack.append(int(stack.pop() / num))

                num = 0
                presign = char


        return sum(stack)




