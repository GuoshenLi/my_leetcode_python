# 为此设计算法如下：
#
# 先统计每一个结点的入度，如果有入度为 2 的结点，考虑删除一条边（根据题目意思，删除的是输入的边的列表中最后出现的），剩下的 有向边 是否形成回路（形成环）。如果不能形成环，就应该删除这条边；
# 在没有如果有入度为 2 的结点的前提下，尝试删除形成入度为 1 的 有向边 （不能删除入度为 0 的有向边），判断剩下的 有向边 是否形成环。


from typing import List
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

        if x_root == y_root:
            return False
        self.parents[x_root] = y_root
        return True


    def hascycle(self, edges, index):
        for i, (u, v) in enumerate(edges):
            if i == index:
                continue
            if not self.union(u, v): return True

        return False



class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        in_degree = [0] * (n + 1)
        for u, v in edges:
            in_degree[v] += 1


        for i in range(n - 1, -1, -1):
            if in_degree[edges[i][1]] == 2:
                uf = UnionFind(n + 1)
                if not uf.hascycle(edges, i):
                    return edges[i]

        for i in range(n - 1, -1, -1):
            if in_degree[edges[i][1]] == 1:
                uf = UnionFind(n + 1)
                if not uf.hascycle(edges, i):
                    return edges[i]

