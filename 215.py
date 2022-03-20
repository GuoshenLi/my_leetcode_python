# 快速选择算法
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            tmp = nums[left]
            while left < right:
                while left < right and tmp <= nums[right]:
                    right -= 1
                nums[left] = nums[right]

                while left < right and nums[left] <= tmp:
                    left += 1
                nums[right] = nums[left]

            nums[left] = tmp

            return left

        k = len(nums) - k  # 第k大=第len(nums)-k小

        left, right = 0, len(nums) - 1

        while True:
            mid = partition(left, right)
            if mid == k:
                return nums[mid]
            elif mid < k:
                left = mid + 1
            else:
                right = mid - 1




from typing import List
import heapq

class Solution:
    # 使用容量为 k 的小顶堆
    # 元素个数小于 k 的时候，放进去就是了
    # 元素个数大于 k 的时候，小于等于堆顶元素，就扔掉，大于堆顶元素，就替换

    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)

        L = []
        for index in range(k):
            # heapq 默认就是小顶堆
            heapq.heappush(L, nums[index])

        for index in range(k, size):
            if nums[index] > L[0]:
                # 看一看堆顶的元素，只要比堆顶元素大，就替换堆顶元素
                heapq.heapreplace(L, nums[index])
                # replace堆顶之后再sift一下调整
        # 最后堆顶中的元素就是堆中最小的，整个数组中的第 k 大元素
        return L[0]
