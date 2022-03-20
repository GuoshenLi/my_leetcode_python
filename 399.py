from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 整一个图

        graph = defaultdict(dict)

        for equa, val in zip(equations, values):
            k, v = equa[0], equa[1]
            graph[k][v] = val
            graph[v][k] = 1 / val

        print(graph)



        def dfs(start, end, visited):
            if start not in graph: return -1
            elif start == end: return 1

            visited.add(start)
            for neighbor in graph[start]:
                if neighbor not in visited:
                    val = dfs(neighbor, end, visited)
                    if val != -1:
                        return graph[start][neighbor] * val

            return -1

        res = []

        for item in queries:
            visited = set()
            res.append(dfs(item[0], item[1], visited))

        return res