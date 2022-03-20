from collections import Counter
from typing import List
# 暴力 超出时间限制
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        unique = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if abs(nums[i] - nums[j]) == k:
                    if nums[i] < nums[j]:
                        unique.add((nums[i], nums[j]))
                    else:
                        unique.add((nums[j], nums[i]))

        return len(unique)


#
# O(n)的解法

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            res = 0
            count_num = Counter(nums)
            for k, v in count_num.items():
                if v > 1:
                    res += 1

            return res


        else:
            res = 0
            unique_nums = set(nums)
            for num in unique_nums:
                if num + k in unique_nums:
                    # 只用考虑绝对值的一边就可以了 因为(i, j) 和(j, i)是一样的
                    res += 1

            return res


print(Solution().findPairs(nums = [3, 1, 4, 1, 5], k = 2))