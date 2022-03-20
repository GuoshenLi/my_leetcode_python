from collections import deque
# bfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        queue = deque()
        queue.append((0, [0]))
        res = []

        while queue:
            node_tup = queue.popleft()
            node = node_tup[0]
            path = node_tup[1]
            if node == target:
                res.append(path)

            for next_node in graph[node]:
                queue.append((next_node, path + [next_node]))

        return res


# dfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        self.target = len(graph) - 1
        self.dfs(0, graph, [])

        return self.res


    def dfs(self, node, graph, path):
        if node == self.target:
            self.res.append(path + [node])
            return None

        for next_node in graph[node]:
            self.dfs(next_node, graph, path + [node])


        return None
