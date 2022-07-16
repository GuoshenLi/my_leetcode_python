class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis=[]
        for l in matrix:
            lis+=l
        lis.sort()

        return lis[k-1]


import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if len(heap) >= k:
                    if -matrix[i][j] > heap[0]:
                        heapq.heapreplace(heap, -matrix[i][j])
                    else:  # 因为数组升序 可以直接break
                        break
                else:
                    heapq.heappush(heap, -matrix[i][j])

        return -heap[0]

# 字节面试题 最优解法 O(n * log(right - left))
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

