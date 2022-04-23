# 牛顿法
from typing import List
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        n, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + n / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(xi)


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