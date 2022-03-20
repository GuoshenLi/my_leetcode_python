# 超时（65/ 68）
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:


        graph = [[] for i in range(n)]
        for k, v in edges:
            graph[k].append(v)
            graph[v].append(k)


        # edges = [[1, 0], [1, 2], [1, 3]]

        # graph = [[1], [0, 2, 3], [1], [1]]
        #           0    1          2    3

        final = []

        res = float('+inf')
        for i in range(n):
            queue = deque()
            visited = set()
            queue.append((i, 0))
            visited.add(i)
            this_res = float('-inf')
            while queue:
                this_point, level = queue.popleft()
                this_res = max(this_res, level)
                for next_point in graph[this_point]:
                    if next_point not in visited:
                        queue.append((next_point, level + 1))
                        visited.add(next_point)


            if this_res < res:
                final = [i]
                res = this_res

            elif this_res == res:
                final.append(i)

        return final


# 拓扑排序变种
from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1: return[0]

        graph = [[] for i in range(n)]
        degree = [0 for i in range(n)]

        for k, v in edges:
            degree[k] += 1
            degree[v] += 1

            graph[k].append(v)
            graph[v].append(k)

        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)


        while n > 2:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for next_node in graph[node]:
                    degree[next_node] -= 1
                    if degree[next_node] == 1:
                        queue.append(next_node)

                n -= 1


        res = []
        while queue:
            res.append(queue.popleft())


        return res








from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1: return[0]

        graph = [[] for i in range(n)]
        degree = [0 for i in range(n)]

        for k, v in edges:
            degree[k] += 1
            degree[v] += 1

            graph[k].append(v)
            graph[v].append(k)

        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)


        while queue:
            res = []
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                res.append(node)

                for next_node in graph[node]:
                    degree[next_node] -= 1
                    if degree[next_node] == 1:
                        queue.append(next_node)


        return res




