# 思路:题目的目标是如何使得数组所有元素组成的表达式运算结果为target,
# 假如我们将数组元素和记为sum,将全部带有+表达式和记为p,
# 全都带有-表达式和记为n,则有p-n=target, p+n=sum.
# 则可推导出p = (sum+target)/2。而sum和target是固定的，
# n自然不难求出，此时问题转化为在nums中找出和为p的组合数


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        if n == 1: return 1 if nums[0] == target or nums[0] == -target else 0
        sum_ = sum(nums)
        if (sum_ + target) % 2 != 0: return 0

        target = (sum_ + target) // 2

        dp = [[0] * (target + 1) for i in range(n + 1)]
        # dp[i][j] 其实就是 前i个数 构成和为j的个数

        # 因为nums中存在0 因此不能确定dp[i][0] 的个数
        dp[0][0] = 1
        # dp[0][1 ~ target] = 0
        # 所以说第0行已经初始化 所以i从1开始
        # 因为nums中存在0 因此不能确定dp[i][0] 的个数 所以要扔进去遍历
        for i in range(1, n + 1):
            weight = nums[i - 1]
            for j in range(target + 1):
                if j - weight >= 0:
                    dp[i][j] = dp[i - 1][j - weight] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]


        return dp[n][target]




class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        @lru_cache(None)
        def dfs(index, tmp):
            if index == n:
                if tmp == target:
                    return 1
                else:
                    return 0
            res = 0

            res += dfs(index + 1, tmp + nums[index])
            res += dfs(index + 1, tmp - nums[index])

            return res

        return dfs(0, 0)








class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        if len(nums) == 1: return 1 if nums[0] == target or nums[0] == -target else 0

        sumValue = sum(nums)
        if target > sumValue or (sumValue + target) % 2 == 1: return 0
        bagSize = (sumValue + target) // 2

        dp = [0] * (bagSize + 1)
        dp[0] = 1

        for num in nums:
            for i in range(bagSize, -1, -1):

                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[bagSize]
