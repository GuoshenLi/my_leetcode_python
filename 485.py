class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0

        return res

# 20260527 双指针 直接秒了
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        right = 0
        res = 0
        while right < len(nums):
            while right < len(nums) and nums[right] == 1:
                right += 1

            res = max(res, right - left)

            left = right

            while left < len(nums) and nums[left] == 0:
                left += 1
            right = left

        return res