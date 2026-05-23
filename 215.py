# 快速选择算法
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right):
            i = randint(left, right)
            nums[i], nums[left] = nums[left], nums[i]
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



# 标准快速选择
class Solution:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        在子数组 [left, right] 中随机选择一个基准元素 pivot
        根据 pivot 重新排列子数组 [left, right]
        重新排列后，<= pivot 的元素都在 pivot 的左侧，>= pivot 的元素都在 pivot 的右侧
        返回 pivot 在重新排列后的 nums 中的下标
        特别地，如果子数组的所有元素都等于 pivot，我们会返回子数组的中心下标，避免退化
        """

        i = randint(left, right)
        pivot = nums[i]

        nums[i], nums[left] = nums[left], nums[i]

        le, ge = left + 1, right
        while True:
            while le <= ge and nums[le] < pivot:
                le += 1

            while le <= ge and nums[ge] > pivot:
                ge -= 1
            # 此时 nums[j] <= pivot

            if le >= ge:
                break

            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1

        nums[left], nums[ge] = nums[ge], nums[left]

        return ge

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        target_index = n - k  # 第 k 大元素在升序数组中的下标是 n - k
        left, right = 0, n - 1  # 闭区间
        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                # 找到第 k 大元素
                return nums[i]
            if i > target_index:
                # 第 k 大元素在 [left, i - 1] 中
                right = i - 1
            else:
                # 第 k 大元素在 [i + 1, right] 中
                left = i + 1


