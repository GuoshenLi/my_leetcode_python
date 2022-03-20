# 动态规划
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('+inf') for _ in range(n)]
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]


# 贪心
# 更容易理解
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # 当前能够覆盖的范围

        begin = 0
        end = 0
        res = 0

        max_pos = 0
        while end < n - 1:
            for i in range(begin, end + 1):
                max_pos = max(max_pos, i + nums[i])

            begin = end + 1
            end = max_pos

            res += 1
        return res
