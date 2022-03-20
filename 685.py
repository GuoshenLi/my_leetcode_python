# 为此设计算法如下：
#
# 先统计每一个结点的入度，如果有入度为 2 的结点，考虑删除一条边（根据题目意思，删除的是输入的边的列表中最后出现的），剩下的 有向边 是否形成回路（形成环）。如果不能形成环，就应该删除这条边；
# 在没有如果有入度为 2 的结点的前提下，尝试删除形成入度为 1 的 有向边 （不能删除入度为 0 的有向边），判断剩下的 有向边 是否形成环。


from typing import List
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        indegree = [0] * (n + 1)
        for k, v in edges:
            indegree[v] += 1
        # 看有没有入度为2的尝试删除一下
        for i in range(n - 1, -1, -1):
            if indegree[edges[i][1]] == 2:
                if not self.has_circle(edges, n, i):
                    return edges[i]

        # 入度为1的每一条都试一下删除
        for i in range(n - 1, -1, -1):
            if indegree[edges[i][1]] == 1:
                if not self.has_circle(edges, n, i):
                    return edges[i]


    def has_circle(self, edges, n, delete_index):
        parent = [-1] * (n + 1)
        rank = [0] * (n + 1)

        for i in range(n):
            if delete_index == i:
                continue
            if self.union(edges[i][0], edges[i][1], parent, rank):
                return True

        return False


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
                rank[y_root] += 1

            return False
        else:
            return True


    def find(self, x, parent):
        while parent[x] != -1:
            x = parent[x]

        return x
