class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        res = []

        for num1 in nums1:
            for num2 in nums2:
                res.append([num1, num2])

        res.sort(key = sum)
        return res[:k]



# python heapq 大根堆 在前面加一个负号
# class BtmkHeap(object):
#     def __init__(self, k):
#         self.k = k
#         self.data = []
#
#     def Push(self, elem):
#         # Reverse elem to convert to max-heap
#         elem = -elem
#         # Using heap algorighem
#         if len(self.data) < self.k:
#             heapq.heappush(self.data, elem)
#         else:
#             topk_small = self.data[0]
#             if elem > topk_small:
#                 heapq.heapreplace(self.data, elem)
#
#     def BtmK(self):
#         return sorted([-x for x in self.data])


import heapq

# 大根堆其实就是添加一个负号
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # 最小 要大根堆
        heap = []

        for num1 in nums1:
            for num2 in nums2:
                if len(heap) >= k:
                    if (num1 + num2) < -heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, [-(num1 + num2), [num1, num2]])
                    else:
                        break
                else:
                    heapq.heappush(heap, [-(num1 + num2), [num1, num2]])


        return list(map(lambda x: x[1], heap))




import heapq
# 大根堆其实就是添加一个负号
# 直接改写比较方法
class Item:
    def __init__(self, num, pair):
        self.num = num
        self.pair = pair

    def __lt__(self, other):
        return self.num > other.num

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        heap = []

        for num1 in nums1:
            for num2 in nums2:
                if len(heap) >= k:
                    if num1 + num2 < heap[0].num:
                        heapq.heappop(heap)
                        heapq.heappush(heap, Item(num1 + num2, [num1, num2]))
                    else:
                        break
                else:
                    heapq.heappush(heap, Item(num1 + num2, [num1, num2]))


        return [heapq.heappop(heap).pair for i in range(k) if heap]
