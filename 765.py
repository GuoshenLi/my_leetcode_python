class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.cc = n

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root: return False
        self.parent[x_root] = y_root
        self.cc -= 1
        return True

    def find(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]
        return x




class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        num_couples = len(row) // 2

        uf = UnionFind(num_couples)
        for i in range(0, len(row), 2):
            uf.union(row[i] // 2, row[i + 1] // 2)

        return num_couples - uf.cc
