class Solution:
    def massage(self, nums: List[int]) -> int:

        # 动态规划
        if not nums: return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        # 打家劫舍
        for i in range(1, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])


        return dp[-1]
