class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0: return False
        target = sum_ // 2
        n = len(nums)
        @lru_cache(None)
        def dfs(index, tmp):
            if index == n: return tmp == target

            if tmp + nums[index] <= target:
                return dfs(index + 1, tmp) or dfs(index + 1, tmp + nums[index])
            else:
                return dfs(index + 1, tmp)


        return dfs(0, 0)





print(Solution().canPartition(nums = [1, 2, 5]))




# 背包问题
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # 背包问题
        target = sum(nums)
        if target % 2 != 0: return False

        target = target // 2
        n = len(nums)

        dp = [[False] * (target + 1) for i in range(n + 1)]
        # dp[i][j] 表示前i个数字能否构成和为j

        for i in range(n + 1):
            dp[i][0] = True
            # 和为0，肯定可以

        for i in range(1, n + 1):
            weight = nums[i - 1]
            for j in range(1, target + 1):
                # 第i-1个数字选与不选
                if j - weight >= 0:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - weight]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0: return False
        target = sum_ // 2
        length = len(nums)

        @lru_cache(None)
        def dfs(index, tmp):
            if tmp == target: return True
            if index == length: return False

            if nums[index] + tmp <= target:
                return dfs(index + 1, tmp) or dfs(index + 1, tmp + nums[index])
            else:
                return dfs(index + 1, tmp)


        return dfs(0, 0)
