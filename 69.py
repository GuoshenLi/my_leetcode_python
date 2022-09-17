# 牛顿法
from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        t = x

        while True:

            t_new = 1 / 2 * (t + x / t)
            if abs(t_new - t) < 1e-7:
                break
            t = t_new

        return int(t_new)

# 二分查找
# 最后一个小于等于它的数

class Solution:
    def mySqrt(self, x: int) -> int:


        left, right = 0, x
        # 找最后一个数字的平方 <= x

        while left < right:
            mid = (left + right + 1) // 2

            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid

        return left


class Solution:
    def helper(self, nums: List[int], target) -> int:
        if target < nums[0]: return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r + 1) // 2

            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        return l

print(Solution().helper(nums=[1, 2, 2, 3, 4, 5, 5, 5, 6, 7], target=2))