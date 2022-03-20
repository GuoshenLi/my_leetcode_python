from collections import Counter


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)

        stack = []
        seen = set()
        for character in s:
            if character not in seen:
                while stack and stack[-1] > character and counter[stack[-1]] > 0:
                    seen.remove(stack.pop())

                seen.add(character)
                stack.append(character)
            counter[character] -= 1

        return ''.join(stack)



