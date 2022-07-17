# 暴力
import bisect
from typing import List
import heapq

# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#
#         res = []
#         for i in range(len(nums) - k + 1):
#             a = nums[i: i + k]
#             a.sort()
#             if k % 2 == 0:
#                 res.append((a[k // 2 - 1] + a[k // 2]) / 2)
#             else:
#                 res.append(a[k // 2])
#
#
#         return res
#
#
# import heapq
# from typing import List
#
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         min_heap,max_heap = [],[]
#
#         # 初始化
#         for i in range(k):
#             heapq.heappush(min_heap,(nums[i], i))
#             n, idx = heapq.heappop(min_heap)
#             heapq.heappush(max_heap, (-n, idx))
#             if len(max_heap) > len(min_heap):
#                 n, idx = heapq.heappop(max_heap)
#                 heapq.heappush(min_heap, (-n, idx))
#
#         res = [(min_heap[0][0]-max_heap[0][0])/2 if k % 2 == 0 else min_heap[0][0] * 1.0]
#
#         for i in range(k,len(nums)):
#             # 如果新数字应该放到最大堆
#             if nums[i] < min_heap[0][0]:
#
#                 heapq.heappush(max_heap,(-nums[i],i))
#                 # 如果要弹出的元素在最小堆中，调整
#                 if nums[i-k] >= min_heap[0][0]:
#                     # 为什么要取等号 其实就是因为num[i] >= min_heap[0][0] 都加入了最小堆
#                     # 相当于大根堆的有效长度比小根堆要大
#                     n,idx = heapq.heappop(max_heap)
#                     heapq.heappush(min_heap,(-n,idx))
#             else:
#                 heapq.heappush(min_heap,(nums[i],i))
#                 # 如果要弹出的元素在最大堆中，调整
#                 # 取等号是特殊情况
#                 if nums[i-k] <= min_heap[0][0]:
#                     n,idx = heapq.heappop(min_heap)
#                     heapq.heappush(max_heap,(-n,idx))
#
#             # 将堆顶在窗口外的元素清除出去
#             while min_heap and min_heap[0][1] <= i-k:
#                 heapq.heappop(min_heap)
#             while max_heap and max_heap[0][1] <= i-k:
#                 heapq.heappop(max_heap)
#
#             # 添加答案
#             res.append((min_heap[0][0]-max_heap[0][0])/2 if k % 2 == 0 else min_heap[0][0] * 1.0)
#
#         return res
#
#
# Solution().medianSlidingWindow(nums = [1,1,2], k = 2)
# Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
#
#
#
# # 滑动窗口 + 二分查找
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         # 滑动窗口 + 二分查找
#         n = len(nums)
#
#         #滑动窗口的开始idx
#         start = 0
#
#         #前k个数先放入window里，排序放好
#         window = sorted(nums[:k])
#         res = [window[k//2]] if k%2 else [(window[k//2] + window[k//2-1])/2]
#
#         for i in range(k, n):
#
#             #对于剩下的数进行操作
#             #每次把nums[i]二分插入进window里
#             #然后二分找到nums[start]移出window
#
#             bisect.insort_right(window, nums[i])
#             index = bisect.bisect_left(window, nums[start])
#             window.pop(index)
#             # 插入从右边插入 删除从左边删除
#             start += 1
#
#             if k%2 == 1:
#                 res.append(window[k//2])
#             else:
#                 res.append((window[k//2] + window[k//2-1])/2)
#
#         return res
#
#
#
# Solution().medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)

# 或者用sortedlist
# 滑动窗口 + 二分查找
from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        window = SortedList(nums[:k])


        start = 0
        res = [window[k // 2]] if k % 2 == 1 else [(window[k // 2] + window[k // 2 - 1]) / 2]

        for i in range(k, n):
            window.add(nums[i])
            index = bisect.bisect_left(window, nums[start])
            window.pop(index)

            start += 1

            if k % 2 == 0:
                res.append((window[k // 2] + window[k // 2 - 1])/ 2)
            else:
                res.append(window[k // 2])

        return res


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        max_heap = []
        min_heap = []
        res = []
        # 保证max_heap 中的元素个数 >= min_heap的元素个数

        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
            tmp_num, idx = heapq.heappop(max_heap)
            heapq.heappush(min_heap, (-tmp_num, idx))
            if len(min_heap) > len(max_heap):
                tmp_num, idx = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (-tmp_num, idx))

        res.append(-max_heap[0][0] if k % 2 == 1 else (min_heap[0][0] - max_heap[0][0]) / 2)


        for i in range(k, len(nums)):

            if nums[i] > -max_heap[0][0]: # 如果比大根堆堆顶要大 严格大
                # 就放入小根堆
                heapq.heappush(min_heap, (nums[i], i))
                # 重点：加的东西在小根堆，删除的东西在大根堆，所以左右两个堆差距为2，就要从大根堆当中拿一个放到小根堆
                # 如果要delete的值在大根堆
                # 一定要等于号
                # 处理特殊情况
                if nums[i - k] <= -max_heap[0][0]:
                    tmp_num, idx = heapq.heappop(min_heap)
                    heapq.heappush(max_heap, (-tmp_num, idx))

            else:
                # 放入大根堆
                heapq.heappush(max_heap, (-nums[i], i))

                # 如果要删除的nums[i - k]在小根堆
                if nums[i - k] >= -max_heap[0][0]:
                    # 一定要等于号
                    # 处理特殊情况
                    tmp_num, idx = heapq.heappop(max_heap)
                    heapq.heappush(min_heap, (-tmp_num, idx))

            while min_heap and min_heap[0][1] <= i - k:
                heapq.heappop(min_heap)

            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            res.append(-max_heap[0][0] if k % 2 == 1 else (min_heap[0][0] - max_heap[0][0]) / 2)

        return res

Solution().medianSlidingWindow(nums = [1,1,1,1], k = 2)



