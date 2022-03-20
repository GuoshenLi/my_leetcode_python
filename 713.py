# 超时 枚举
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0
        for i in range(len(nums)):
            ans = 1
            for j in range(i, len(nums)):
                ans *= nums[j]
                if ans < k:
                    res += 1
                else:
                    break

        return res


# 双指针
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        res = 0
        left = 0
        product = 1

        # 一直统计以右指针为端点的连续子数组有多少个

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1

            res += (right - left + 1)
        return res


