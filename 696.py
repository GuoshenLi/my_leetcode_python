class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 对字符进行分组
        cache = []

        flag = s[0]
        count = 1
        for char in s[1:]:
            if flag == char:
                count += 1
            else: # 碰到不相等的
                cache.append(count)
                count = 1
                flag = char
        cache.append(count)

        res = 0
        for i in range(1, len(cache)):
            res += min(cache[i - 1], cache[i])
        return res

# 双指针
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        nums = []

        right = 0
        left = 0

        while right < len(s):
            while right < len(s) and s[right] == s[left]:
                right += 1
            nums.append(right - left)

            left = right

        res = 0
        for i in range(1, len(nums)):
            res += min(nums[i], nums[i - 1])

        return res