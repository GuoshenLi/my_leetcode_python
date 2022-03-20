# 高频题 各大厂
# 滑动窗口

# 维护left 和 right指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left, right = 0, 0
        n = len(s)
        max_len = 0

        while right < n:
            while right < n and s[right] not in unique:
                unique.add(s[right])
                right += 1

            max_len = max(max_len, len(unique))
            unique.remove(s[left])
            left += 1

        return max_len


# 遍历法
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = 0
        n = len(s)
        for first in range(n):
            unique = set()
            for second in range(first, n):
                if s[second] not in unique:
                    unique.add(s[second])
                else:
                    break
            length = max(len(unique), length)

        return length
