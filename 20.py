class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        table = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:

            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if not stack: return False
                if stack[-1] != table[char]: return False
                stack.pop()

        return len(stack) == 0

