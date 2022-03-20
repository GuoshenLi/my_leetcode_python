# 简单的dfs
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj_list = [[] for i in range(n)]
        for u, v in richer:
            adj_list[v].append(u)

        memo = {}
        def dfs(index):

            if index in memo: return memo[index]

            min_quiet_index = index
            for next_index in adj_list[index]:
                try_index = dfs(next_index)
                if quiet[try_index] < quiet[min_quiet_index]:
                    min_quiet_index = try_index

            memo[index] = min_quiet_index
            return memo[index]


        res = [0] * n
        for i in range(n):
            res[i] = dfs(i)

        return res


# 拓扑排序
from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj_list = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]
        res = [i for i in range(n)]
        for u, v in richer:
            adj_list[u].append(v)
            in_degree[v] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)


        while queue:
            node = queue.popleft()

            for next_node in adj_list[node]:
                if quiet[res[node]] < quiet[res[next_node]]:
                    res[next_node] = res[node]


                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    queue.append(next_node)

        return res