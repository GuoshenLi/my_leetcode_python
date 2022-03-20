class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        dp = [[float('+inf')] * (m + 1) for i in range(n)]
        # dp[i][j] 其实就是从nums[0] 到 nums[i] 分成j个组，所形成的和的最大值的最小值。
        # 分成一个组 直接为和
        for i in range(n):
            dp[i][1] = pre_sum[i + 1]

        for i in range(n):
            for j in range(2, m + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], pre_sum[i + 1] - pre_sum[k + 1]))

        return dp[-1][-1]
