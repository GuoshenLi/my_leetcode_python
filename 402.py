class Solution:
    def removeKdigits(self, num: str, k: int) -> str:


        stack = []
        remain = len(num) - k
        for character in num:
            while stack and k and character < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(character)

        return ''.join(stack[:remain]).lstrip('0') or '0'

