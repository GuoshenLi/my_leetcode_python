class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')

        for i in range(len(nums)):
            sum_ = 0
            for j in range(i, len(nums)):
                sum_ += nums[j]
                max_sum = max(max_sum, sum_)

        return max_sum

# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)



# 贪心算法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = float('-inf')
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            max_ = max(sum_, max_)
            if sum_ < 0:
                sum_ = 0

        return max_



