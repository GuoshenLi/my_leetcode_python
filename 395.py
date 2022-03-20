# 滑动窗口
# 本题的滑动窗口解法和迄今为止做的滑动窗口题目的最大不同，本题需要手动增加限# 制，即限制窗口内字符种类。才可能做滑动窗口，否则压根收缩不了左边

from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        for i in range(1, len(set(s)) + 1):
            # 要限制窗口内不同元素的种类
            window = defaultdict(int)
            left, right, diff_count, k_count = 0, 0, 0, 0
            # diff_count 记录当前window当中有多少个不同的字符
            # k_count 记录当前window当中有说个数量满足大于等于k的字符
            while right < len(s):
                window[s[right]] += 1
                if window[s[right]] == 1:
                    diff_count += 1
                if window[s[right]] == k:
                    k_count += 1
                right += 1

                while diff_count > i:
                    if window[s[left]] == 1:
                        diff_count -= 1
                    if window[s[left]] == k:
                        k_count -= 1
                    window[s[left]] -= 1

                    left += 1

                if k_count == i:
                    res = max(res, right - left)

        return res







# 暴力
# 通过 28 / 32
from collections import defaultdict, Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        n = len(s)
        length = 0
        for left in range(n):
            for right in range(left, n):
                count = Counter(s[left: right + 1])
                if all(v >= k for v in count.values()):
                    length = max(length, right - left + 1)

        return length

