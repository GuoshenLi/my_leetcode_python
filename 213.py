class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        # 分情况：抢开头，不抢结尾
        #      ：抢结尾，不抢开头
        #      ：开头结尾都不抢

        return max(self.helper(nums[:-1]), self.helper(nums[1:]), self.helper(nums[1:-1]))

    def helper(self, nums):
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i], dp[i - 1], dp[i - 2] + nums[i])

        return max(dp)
