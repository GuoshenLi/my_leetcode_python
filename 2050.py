import heapq
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]

        for u, v in relations:
            u -= 1
            v -= 1
            graph[u].append(v)
            in_degree[v] += 1


        heap = [(time[i], i) for i in range(n) if in_degree[i] == 0]
        heapq.heapify(heap)

        while heap:
                t, index = heapq.heappop(heap)
                for neighbor in graph[index]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        heapq.heappush(heap, (t + time[neighbor], neighbor))

        return t