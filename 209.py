# 前缀和
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        res = float('+inf')

        for i in range(1 + n):
            for j in range(i + 1, 1 + n):
                if pre_sum[j] - pre_sum[i] >= target:
                    res = min(j - i, res)
                    break

        if res == float('+inf'):
            return 0
        else:
            return res

# 二分搜索
# 前缀和
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        res = float('+inf')

        for i in range(1 + n):
            index = self.binary_search(pre_sum, i + 1, n, target + pre_sum[i])
            if index != -1:
                res = min(res, index - i)


        if res == float('+inf'):
            return 0
        else:
            return res


    def binary_search(self, nums, left, right, target):
        if target > nums[right]: return -1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid



        return left





class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        res = float('+inf')
        temp = 0

        while right < len(nums):

            temp += nums[right]

            while temp >= target:
                res = min(res, right - left + 1)
                temp -= nums[left]
                left += 1

            right += 1

        return res if res != float('+inf') else 0



class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        n = len(nums)
        left = 0
        right = 0

        # window: [left, right)

        res = float("+inf")
        sum_ = 0

        while right < n:
            sum_ += nums[right]
            right += 1

            while sum_ >= target:
                res = min(res, right - left)
                sum_ -= nums[left]
                left += 1

        return 0 if res == float("+inf") else res


print(Solution().minSubArrayLen(target=7, nums=[2,3,1,2,4,3]))