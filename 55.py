# 贪心
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_dis = 0
        for i in range(len(nums)):
            if i > max_dis:
                return False
            max_dis = max(max_dis, i + nums[i])
        return True

# 倒序遍历
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 2, - 1, -1):
            if nums[i] + i >= last:
                last = i

        return last == 0

# 动态规划
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for i in range(n)]

        dp[0] = True

        for i in range(1, n):
            for j in range(i):
                if dp[j] == True and j + nums[j] >= i:
                    dp[i] = True
                    break

        return dp[-1]






