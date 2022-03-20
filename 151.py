class Solution:
    def reverseWords(self, s: str) -> str:

        return ' '.join(s.split()[::-1])
        # 注意split大法

# 双指针
class Solution:
    def reverseWords(self, s: str) -> str:

        left = 0
        right = len(s) - 1
        res = ''
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        i = j = right
        while i >= left:
            while i >= left and s[i].isalnum():
                i -= 1

            res += ' ' + s[i + 1: j + 1]

            while i >= left and s[i] == ' ':
                i -= 1
            j = i
        return res[1:]






