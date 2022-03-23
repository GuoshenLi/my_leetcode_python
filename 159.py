from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3: return n

        max_len = 0
        left, right = 0, 0
        window = defaultdict(int)
        valid = 0

        while right < n:

            window[s[right]] += 1
            if window[s[right]] == 1:
                valid += 1
            right += 1

            while valid >= 3:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    valid -= 1
                left += 1

            max_len = max(max_len, right - left)

        return max_len

