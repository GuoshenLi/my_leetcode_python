# 双指针
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        res = 0
        left = 0
        product = 1
        right = 0

        # 一直统计以右指针为端点的连续子数组有多少个

        while right < len(nums):
            product *= nums[right]
            right += 1
            while product >= k:
                product /= nums[left]
                left += 1

            res += (right - left)
        return res