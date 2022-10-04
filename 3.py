class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        table = set()

        left = right = 0
        max_len = 0

        while right < len(s):
            while right < len(s) and s[right] not in table:
                table.add(s[right])
                right += 1

            max_len = max(max_len, right - left)
            table.remove(s[left])
            left += 1


        return max_len