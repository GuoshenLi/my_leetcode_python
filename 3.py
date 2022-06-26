class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0

        right = 0
        left = 0

        n = len(s)
        window = set()

        while right < n:
            if s[right] not in window:
                window.add(s[right])
                right += 1

            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1


            max_len = max(max_len, right - left)

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        table = set()

        left, right = 0, 0
        res = 0

        while right < n:

            while right < n and s[right] not in table:
                table.add(s[right])
                right += 1

            res = max(res, right - left)

            while right < n and s[right] in table:
                table.remove(s[left])
                left += 1

        return res