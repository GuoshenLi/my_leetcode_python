from collections import defaultdict
# 字节跳动笔试题目
# O(n ** 2)时间复杂度
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # 字符串合法 能替换
        def valid_string():
            return sum(num.values()) - max(num.values()) <= k

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


#O(n) 时间复杂度
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26
        n = len(s)
        res = max_number = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            max_number = max(max_number, num[ord(s[right]) - ord("A")])
            right += 1

            while right - left - max_number > k:
                num[ord(s[left]) - ord("A")] -= 1
                left += 1

            res = max(res, right - left)
        return res


from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window = defaultdict(int)
        left = 0
        right = 0
        max_number = 0
        res = 0

        while right < len(s):
            window[s[right]] += 1
            max_number = max(max_number, window[s[right]])
            right += 1

            while right - left - max_number > k:
                window[s[left]] -= 1
                left += 1

            res = max(res, right - left)

        return res

print(Solution().characterReplacement(s = "AABABBA", k = 1))