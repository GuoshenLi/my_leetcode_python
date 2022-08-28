from collections import deque


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        queue = deque()
        in_degree = [0 for i in range(n)]
        graph = [[] for i in range(n)]

        for u, v in relations:
            u = u - 1
            v = v - 1
            graph[u].append(v)
            in_degree[v] += 1
        count_course = 0
        count_semester = 0
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()
                count_course += 1
                for neighbor in graph[index]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            count_semester += 1

        return count_semester if count_course == n else -1



