from collections import deque

# bfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for i in range(n)]
        visited = [False] * n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        count = 0
        for i in range(n):
            if visited[i] == False:
                count += 1

                queue = deque()
                queue.append(i)
                visited[i] = True
                while queue:
                    index = queue.popleft()
                    for neighbor in graph[index]:
                        if visited[neighbor] == False:
                            queue.append(neighbor)
                            visited[neighbor] = True
        return count

# dfs
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for i in range(n)]
        visited = [False] * n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(index):
            visited[index] = True
            for neighbor in graph[index]:
                if visited[neighbor] == False:
                    dfs(neighbor)

        count = 0
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                count += 1
        return count



# 并查集
class UnionFind:
    def __init__(self, length):
        self.length = length
        self.parents = [-1] * self.length
        self.cc = length

    def find(self, x):
        while self.parents[x] != -1:
            x = self.parents[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root: return False
        self.parents[x_root] = y_root
        self.cc -= 1
        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.cc




