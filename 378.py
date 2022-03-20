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

