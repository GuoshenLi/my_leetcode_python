# 暴力解法
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        count = 0

        for start in range(len(nums) - 2):
            diff = nums[start + 1] - nums[start]

            for end in range(start + 2, len(nums)):
                for i in range(start + 1, end + 1):
                    if nums[i] - nums[i - 1] != diff:
                        break
                else:
                    count += 1

        return count




# 优化的暴力
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        count = 0

        for start in range(len(nums) - 2):
            diff = nums[start + 1] - nums[start]
            for end in range(start + 2, len(nums)):
                if nums[end] - nums[end - 1] == diff:
                    count += 1
                else:
                    break

        return count

# 动态规划
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        # dp[i] 存储以i结尾的等差数列的个数
        n = len(nums)
        dp = [0 for i in range(n)]

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1

        return sum(dp)



class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] += (dp[i - 1] + 1)
                # 和子序列一样的写法

        return sum(dp)