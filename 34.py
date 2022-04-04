# 第一个大于等于target 最后一个小于等于target.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums: return res
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] != target: return res

        res[0] = left

        left = 0
        right = n - 1

        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        res[1] = left

        return res
