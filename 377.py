# 可以记忆化递归

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)

        @lru_cache(None)
        def dfs(index, tmp):
            if tmp == target:
                return 1

            res = 0
            for i in range(n):
                # 求排列从0 ~ n
                # 求组合从index 到 n
                if tmp + nums[i] <= target:
                    res += dfs(i, tmp + nums[i])

            return res

        return dfs(0, 0)



class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        n = len(nums)
        dp = [[0] * (target + 1) for i in range(n + 1)]
        # dp[i][j] 前i个凑成j
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j >= nums[i - 1]:
                    for k in range(i):
                        if j - nums[k] >= 0:
                            dp[i][j] += dp[i][j - nums[k]]

                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]




class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]



        return dp[-1]