from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # count 一下 再加上最大的奇数

        count_s = Counter(s)

        count = 0
        has_odd = False

        for v in count_s.values():
            if v % 2 == 0:
                count += v
            else:
                count += v - 1
                has_odd = True

        if has_odd == True:
            count += 1

        return count
