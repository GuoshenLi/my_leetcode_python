# 超时 暴力解法
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        n = len(nums)
        if k == n:
            return sum(nums) / k

        i = 0
        j = i + k
        max_mean = float('-inf')

        while j <= n:
            max_mean = max(max_mean, sum(nums[i:j]) / k)
            j += 1
            i += 1

        return max_mean

# 滑动窗口
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k

