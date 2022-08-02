class UnionFind:
    def __init__(self, length):
        self.length = length
        self.parent = [-1] * self.length

    def find(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]

        return x

    def union(self, x, y):

        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: return False

        self.parent[root_x] = root_y
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        uf = UnionFind(n)
        for u, v in edges:
            if uf.union(u, v):
                count += 1

        return n - count


from collections import deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0

        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                count += 1
                queue = deque()
                queue.append(i)
                while queue:
                    index = queue.popleft()
                    for neighbor in graph[index]:
                        if visited[neighbor] == False:
                            visited[neighbor] = True
                            queue.append(neighbor)

        return count



from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        visited = [False] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = 0

        def dfs(index):
            visited[index] = True
            for neighbor in graph[index]:
                if visited[neighbor] == False:
                    dfs(neighbor)

        for i in range(n):
            if visited[i] == False:
                count += 1
                dfs(i)

        return count

