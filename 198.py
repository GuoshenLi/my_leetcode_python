class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]



        dp = [0] * n
        # dp[i] 截止到i为止，能抢到的最大金额数目
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # 不抢nums[i] 延续dp[i - 1]
            # 抢nums[i] 就要从dp[i - 2] 转换
        return dp[n - 1]