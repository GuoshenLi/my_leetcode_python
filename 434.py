class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

# 记录开头即可
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i in range(len(s)):

            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                count += 1

        return count



class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        left, right = 0, len(s) - 1


        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        i = j = left
        while j <= right:
            while j <= right and s[j] != ' ':
                j += 1

            count += 1
            while j <= right and s[j] == ' ':
                j += 1

            i = j

        return count

