from typing import List
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while i - q[0][1] >= k:
                # 维持窗口大小为3
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


print(Solution().maxSlidingWindow(nums = [3,1,-1,5], k = 3))





# 2022.7.17 我已不再是从前那个少年
# O(nlog(k))
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = []
        res = []
        for i in range(len(nums)):

            heapq.heappush(heap, (-nums[i], i))
            if len(heap) >= k:
                while heap[0][1] < i - k + 1:
                    heapq.heappop(heap)
                res.append(-heap[0][0])

        return res



from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        res = []
        # 维护一个单调递减双端队列
        # 队列的第一个元素是滑动窗口最大值的下标
        for i in range(len(nums)):
            # 如果下标超出窗口范围，要pop
            if queue and queue[0] <= i - k:
                queue.popleft()
            # 维护单调递减队列
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            # 加入
            queue.append(i)
            # 满足k个了 再append 进去
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res

# 二维 最大池化 O(n ** 2)
from collections import deque
class Solution:
    def maxSlidingMatrix(self, matrix: List[List[int]], k_row: int, k_col:int) -> List[List[int]]:

        row_result = []
        for row in matrix:
            row_result.append(self.maxSlidingWindow(row, k_col))
        row_result_transpose = self.transpose(row_result)
        result_transpose = []
        for col in row_result_transpose:
            result_transpose.append(self.maxSlidingWindow(col, k_row))

        return self.transpose(result_transpose)


    def transpose(self, matrix):
        if not matrix: return [[]]
        m = len(matrix)
        n = len(matrix[0])

        transpose_matrix = [[0] * m for i in range(n)]
        for i in range(m):
            for j in range(n):
                transpose_matrix[j][i] = matrix[i][j]

        return transpose_matrix


    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = deque()
        res = []
        # 维护一个单调递减双端队列
        # 队列的第一个元素是滑动窗口最大值的下标
        for i in range(len(nums)):
            # 如果下标超出窗口范围，要pop
            if queue and queue[0] <= i - k:
                queue.popleft()
            # 维护单调递减队列
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            # 加入
            queue.append(i)
            # 满足k个了 再append 进去
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res

print(Solution().maxSlidingMatrix(matrix=[[1,2,3,4,5,1,2,3,233,443],
                                          [1,2,3,4,5,1,2,3,233,443],
                                          [1,2,3,4,5,1,2,3,233,443],
                                          [1,2,3,4,5,1,2,3,233,443],
                                          [1,2,3,4,5,1,2,3,233,443]],
                                        k_row=3,
                                        k_col=4))