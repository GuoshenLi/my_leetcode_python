# 维护一个最小堆
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            if len(self.heap) >= self.k:
                if num > self.heap[0]:
                    heapq.heapreplace(self.heap, num)
            else:
                heapq.heappush(self.heap, num)




    def add(self, val: int) -> int:
        if len(self.heap) >= self.k:
            if val > self.heap[0]:
                heapq.heapreplace(self.heap, val)
        else:
            heapq.heappush(self.heap, val)

        return self.heap[0]

