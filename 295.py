import heapq


class MedianFinder:

    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if len(self.min_heap) > len(self.max_heap):
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return (self.min_heap[0] + self.max_heap[0][1]) / 2
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return self.max_heap[0][1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# python 最大堆注意负号
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = [] #max_heap 一定要加 负 号

    def addNum(self, num: int) -> None:
        # 来一个数字 先加到最大堆，然后pop最大堆的堆顶加到最小堆
        # 看最小堆长度是否比最大堆长度大
        # 如果大则 pop最小堆的堆顶 加到最大堆

        heapq.heappush(self.max_heap, -num)
        tmp_num = heapq.heappop(self.max_heap)
        tmp_num = -tmp_num # the true value
        heapq.heappush(self.min_heap, tmp_num)
        if len(self.min_heap) > len(self.max_heap):
            tmp_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -tmp_num)



    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2

        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()