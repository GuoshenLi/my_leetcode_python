from collections import defaultdict
# 字节跳动笔试题目

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # 字符串合法 能替换
        def valid_string():
            return sum(num.values()) - max(num.values())

        num = defaultdict(int)
        n = len(s)
        res = left = right = 0
        # right  left 要同时更新，窗口要变大 不能变小
        while right < n:
            num[s[right]] += 1
            right += 1
            # 如果窗口合法 右指针往右移动 尝试扩大窗口，
            # 如果窗口不合法 左右指针同时往右移动 尝试下一个窗口 不能缩小窗口！因为找最大的
            while not valid_string():
                num[s[left]] -= 1
                left += 1

            res = max(res, right - left)
        return res


print(Solution().characterReplacement(s = "AABABBA", k = 1))