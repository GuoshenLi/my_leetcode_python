from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        maga_count = Counter(magazine)
        for char in ransomNote:
            if char not in maga_count:
                return False
            elif char in maga_count and maga_count[char] == 0:
                return False
            else:
                maga_count[char] -= 1

        return True


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        maga_count = [0 for _ in range(26)]

        for char in magazine:
            maga_count[ord(char) - ord('a')] += 1

        for char in ransomNote:
            if maga_count[ord(char) - ord('a')] == 0:
                return False
            else:
                maga_count[ord(char) - ord('a')] -= 1

        return True




