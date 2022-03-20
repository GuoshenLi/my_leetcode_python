# 另外一题目：和最大子数组

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1 # or 1的作用是，当nums[i - 1]==0时，nums[i]乘等自身
            nums_reverse[i] *= nums_reverse[i - 1] or 1
        return max(max(nums),max(nums_reverse))

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [0 for i in range(n)]
        dp_min = [0 for i in range(n)]

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])

        return max(dp_max)


