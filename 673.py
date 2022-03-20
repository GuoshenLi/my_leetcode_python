# 比300更难 最长上升子序列的个数
# 基本递归问题　
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 1

        dp = [1] * n
        count = [1] * n


        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    # 还有一种情况就是dp[j] + 1 < dp[i] 这种情况就不用管了
        max_length = max(dp)

        res = 0
        for i in range(n):
            if dp[i] == max_length:
                res += count[i]
        return res

