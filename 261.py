class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n个节点 至少要n - 1条边
        if len(edges) < n - 1: return False
        parent = [-1] * n
        # 判断无向图是否有环 典型的并查集
        def find_root(x):
            while parent[x] != -1:
                x = parent[x]
            return x

        def union_vertices(x, y):
            x_root = find_root(x)
            y_root = find_root(y)

            if x_root == y_root: return False
            parent[x_root] = y_root
            return True

        for u, v in edges:
            if not union_vertices(u, v):
                return False

        return True