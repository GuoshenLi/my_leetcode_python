class UnionFind:
    def __init__(self, length):
        self.length = length
        self.parents = [-1] * self.length

    def find(self, x):
        while self.parents[x] != -1:
            x = self.parents[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root: return False
        self.parents[x_root] = y_root
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        uf = UnionFind(len(edges))

        for u, v in edges:
            if not uf.union(u - 1, v - 1): return [u, v]








