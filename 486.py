# 又是玩游戏 博弈论 记忆化递归
# 局部最优不等于全局最优！ 不能简单地每一次选左右最大的 ！[1, 5, 233, 7]
class Solution:
    # dfs用来记录先手能够赢后手多少分
    # 然后枚举所有可能
    # 暴力递归
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def dfs(l, r):
            if l == r:
                return nums[l]
            # 必须要 - 号， 表明对方去选，就像以前的游戏用not一样
            pickL = nums[l] - dfs(l + 1, r)
            pickR = nums[r] - dfs(l, r - 1)

            return max(pickL, pickR)

        return dfs(0, len(nums) - 1) >= 0




# 又是玩游戏 博弈论 记忆化递归
# dfs用来记录当前玩家在l到r范围内选择，能够赢对方的最大分数
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = [[None] * len(nums) for _ in range(len(nums))]
        def dfs(l, r):
            if l == r:
                return nums[l]

            if memo[l][r]:
                return memo[l][r]

            pickL = nums[l] - dfs(l + 1, r)
            pickR = nums[r] - dfs(l, r - 1)


            memo[l][r] = max(pickL, pickR)
            return memo[l][r]

        return dfs(0, len(nums) - 1) >= 0

