from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1

        return len(nums) - 1
# 二分法 死背 迭代
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]: # 或者大于等于都可以
                right = mid
            else:
                left = mid + 1

        # 如果mid > mid + 1 很明显峰值在右边 所以right = mid
        # 如果mid < mid + 1 很明显峰值在左边 所以left = mid + 1

        return left

# 递归
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        def helper(left, right):
            if left == right:
                return left

            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return helper(left, mid)
            else:
                return helper(mid + 1, right)

        return helper(0, len(nums) - 1)




