# modified dijkstra
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k = k - 1
        adj_list = [[] for i in range(n)]
        dis = [float('+inf') for i in range(n)]
        dis[k] = 0
        for u, v, w in times:
            u, v, w = u - 1, v - 1, w

            adj_list[u].append([v, w])


        heap = [[0, k]]

        while heap:
            distance, u = heapq.heappop(heap)
            if distance > dis[u]: continue
            for v, w in adj_list[u]:
                if dis[v] > distance + w:
                    dis[v] = distance + w
                    heapq.heappush(heap, [dis[v], v])

        res = max(dis)
        return -1 if res == float('+inf') else res

