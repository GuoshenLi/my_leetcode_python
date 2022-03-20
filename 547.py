from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1

        return circles


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.num_group = n
        parent = [-1] * n
        rank = [0] * n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    self.union(i, j, parent, rank)

        return self.num_group

    def union(self, x, y, parent, rank):

        x_root = self.find(x, parent)
        y_root = self.find(y, parent)

        if x_root != y_root:
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root

            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root

            else:
                parent[x_root] = y_root
                rank[x_root] += 1

            self.num_group -= 1


    def find(self, x, parent):
        while parent[x] != -1:
            x = parent[x]

        return x


