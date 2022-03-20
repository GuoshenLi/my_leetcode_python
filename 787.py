# k 步 Dijkstra
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj_list = [[] for i in range(n)]
        for u, v, w in flights:
            adj_list[u].append((v, w))

        k += 1
        min_dis = [[float('+inf')] * (k + 1) for i in range(n)]
        for i in range(k + 1):
            min_dis[src][i] = 0

        heap = [(0, src, 0)]  # distance, src, transfer

        while heap:
            distance, u, num_transfer = heapq.heappop(heap)
            for v, w in adj_list[u]:
                if num_transfer + 1 <= k and min_dis[v][num_transfer + 1] > distance + w:
                    min_dis[v][num_transfer + 1] = distance + w
                    heapq.heappush(heap, (min_dis[v][num_transfer + 1], v, num_transfer + 1))


        return -1 if min(min_dis[dst]) == float('+inf') else min(min_dis[dst])