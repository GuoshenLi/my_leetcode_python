# 暴力解法
from typing import List
import random
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if lower <= sum(nums[i: j + 1]) <= upper:
                    res += 1


        return res





class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        n = len(nums)
        self.lower = lower
        self.upper = upper
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        return self.merge_sort(pre_sum, 0, n)


    def merge_sort(self, nums, left, right):
        if left >= right: return 0

        mid = (left + right) // 2
        left_count = self.merge_sort(nums, left, mid)
        right_count = self.merge_sort(nums, mid + 1, right)
        cross_count = self.calculate(nums, left, mid, right)
        return left_count + right_count + cross_count

    def calculate(self, nums, low, mid, high):

        count = 0
        left = low

        first = mid + 1
        second = mid + 1

        # 所以先写while循环遍历左有序数组
        while left <= mid:
            while first <= high and nums[first] - nums[left] < self.lower:
                # 一定要 nums[first] - nums[left] >= self.lower
                # 的取反，要好好品一下！！！
                # first代表第一个满足nums[first] - nums[left] >=
                # self.lower 的位置
                first += 1



            while second <= high and nums[second] - nums[left] <= self.upper:


                # second代表最后一个满足nums[second] - nums[left] <=
                # self.upper 的位置 + 1

                second += 1
            # 因此满足情况的个数为second - first 个
            count += (second - first)
            left += 1


        left = low
        right = mid + 1
        tmp = []

        while left <= mid and right <= high:

            if nums[right] < nums[left]:
                tmp.append(nums[right])
                right += 1
            else:
                tmp.append(nums[left])
                left += 1

        while left <= mid:
            tmp.append(nums[left])
            left += 1

        while right <= high:
            tmp.append(nums[right])
            right += 1

        nums[low: high + 1] = tmp

        return count
