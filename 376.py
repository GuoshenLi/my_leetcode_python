# O(n^2) 的动态规划
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1] * n
        down = [1] * n
        # dp[i]表明以i结束的最长摆动子序列的长度
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)


        return max(max(up), max(down))


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [1] * n
        down = [1] * n

        # 假设函数 dp[i] 表示 下标0到i的摆序列最长的长度。

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                down[i] = down[i - 1]
                up[i] = down[i - 1] + 1

            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1

            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])
