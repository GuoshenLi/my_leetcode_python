class Solution:
    def reverseVowels(self, s: str) -> str:

        vow = {'a', 'e', 'i', 'o', 'u',
               'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] not in vow and s[right] not in vow:
                left += 1
                right -= 1
            elif s[left] not in vow:
                left += 1
            elif s[right] not in vow:
                right -= 1
            else:
                # 两个都在
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


