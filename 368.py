from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        memo = {}
        n = len(nums)
        nums.sort()

        # 以下标i结尾的最大整除子集

        def dfs(i):
            if i in memo: return memo[i]
            max_subset = []

            for p in range(i):
                if nums[i] % nums[p] == 0:
                    tmp = dfs(p)
                    if len(tmp) > len(max_subset):
                        max_subset = tmp[:]

            memo[i] = max_subset + [nums[i]]
            return memo[i]

        return max([dfs(p) for p in range(n)], key=len)


print(Solution().largestDivisibleSubset(nums = [2,3,4,9,8]))

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = len(nums)

        dp = [1 for i in range(n)]
        dp_ = [[nums[i]] for i in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        dp_[i] = dp_[j] + [nums[i]]

        max_len = max(dp)
        for i in range(n):
            if dp[i] == max_len:
                return dp_[i]



print(Solution().largestDivisibleSubset(nums = [1,2,4,8]))