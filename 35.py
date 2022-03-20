# 找第一个大于等于它的数的下标
class Solution:

    def searchInsert(self, nums, target):
        if target > nums[-1]: return len(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left
