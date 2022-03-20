from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        nums.sort()
        gap = 0
        for i in range(1, n):
            gap = max(gap, nums[i] - nums[i - 1])

        return gap



# 桶排序 很难 很难
# 找到最大的gap 但是要分桶 要让分桶之后 最大的gap出现在桶与桶之间 而不是桶与桶之内 这点很重要
# 分桶一定要保证桶内间隙小于桶间间隙

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        # 一些初始化
        max_ = max(nums)
        min_ = min(nums)
        max_gap = 0

        each_bucket_len = max(1,(max_-min_) // (len(nums)-1))
        buckets =[[] for _ in range((max_-min_) // each_bucket_len + 1)]

        # 把数字放入桶中
        for i in range(len(nums)):
            loc = (nums[i] - min_) // each_bucket_len
            buckets[loc].append(nums[i])

        # 遍历桶更新答案
        prev_max = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and prev_max != float('inf'):
                max_gap = max(max_gap, min(buckets[i]) - prev_max)

            if buckets[i]:
                prev_max = max(buckets[i])

        return max_gap



class Solution:
    def radixSort(self, arr):
        size = len(str(max(arr)))

        for i in range(size):
            buckets = [[] for _ in range(10)]
            for num in arr:
                buckets[num // (10 ** i) % 10].append(num)
            arr.clear()
            for bucket in buckets:
                for num in bucket:
                    arr.append(num)

        return arr

    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        arr = self.radixSort(nums)
        return max(arr[i] - arr[i-1] for i in range(1, len(arr)))



print(Solution().maximumGap(nums = [3, 6, 9, 1]))