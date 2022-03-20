from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        adj_list = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]
        for i in range(n):
            for connect in graph[i]:
                adj_list[connect].append(i)
                in_degree[i] += 1

        queue = deque()

        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for next_node in adj_list[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)
        res = []
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)

        return res