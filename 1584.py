# 最小生成树 prim 算法 模版
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0

        adj_matrix = [[] * n for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_matrix[i].append((j, w))
                adj_matrix[j].append((i, w))

        lowcost = [float("+inf") for i in range(n)]
        visited = [False for i in range(n)]
        heap = [(0, 0)]

        while heap:
            distance, u = heapq.heappop(heap)
            if visited[u] == True: continue
            visited[u] = True
            res += distance

            for v, w in adj_matrix[u]:
                if visited[v] == False and lowcost[v] > w:
                    lowcost[v] = w
                    heapq.heappush(heap, (w, v))

        return res

# kruskal 算法 没多难。。。
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.rank = [1] * n

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parents[x_root] = y_root
            elif self.rank[x_root] > self.rank[y_root]:
                self.parents[y_root] = x_root
            else:
                self.parents[y_root] = x_root
                self.rank[y_root] += 1
            return True
        else:
            return False

    def find(self, x):
        while self.parents[x] != -1:
            x = self.parents[x]
        return x


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        calculate_distance = lambda point1, point2: abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append([calculate_distance(points[i], points[j]), i, j])

        edges.sort()
        uf = UnionFind(n)
        length = 0
        count = 0
        for i in range(len(edges)):

            if uf.union(edges[i][1], edges[i][2]):
                length += edges[i][0]
                count += 1
                if count == n - 1:
                    break
        return length