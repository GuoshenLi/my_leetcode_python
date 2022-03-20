from typing import List

# 题目从编号 1开始
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        length = len(edges)
        parents = [-1] * (length + 1)
        rank = [0] * (length + 1)

        for u, v in edges:
            if not self.union(u, v, parents, rank):
                return [u, v]
        return []

    def find_root(self, x, parents):
        while parents[x] != -1:  # 如果等于-1 证明自己是根
            x = parents[x]
        return x

    def union(self, x, y, parents, rank):
        x_root = self.find_root(x, parents)
        y_root = self.find_root(y, parents)
        if x_root == y_root:
            return False

        else:  # 没有环
            if rank[x_root] > rank[y_root]:
                parents[y_root] = x_root
            elif rank[y_root] > rank[x_root]:
                parents[x_root] = y_root
            else:
                parents[x_root] = y_root
                rank[y_root] += 1

            return True


Solution().findRedundantConnection([[1,2], [1,3], [2,3]])




# 并查集标准代码
def find_root(x, parent):
    while parent[x] != -1: # 如果等于-1 证明自己是根
        x = parent[x]
    return x

def union(x, y, parent, rank):
    x_root = find_root(x, parent)
    y_root = find_root(y, parent)

    if x_root == y_root:
        return False
    else:
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[y_root] > rank[x_root]:
            parent[x_root] = y_root
        else:
            parent[x_root] = y_root
            rank[y_root] += 1

        return True


if __name__ == '__main__':

    vertices = 6
    parent = [-1] * vertices
    rank = [0] * vertices
    edges = [[0, 1],[1, 2],[1, 3],[2, 4],[3, 4],[2, 5]]
    for v1, v2 in edges:
        if not union(v1, v2, parent, rank):
            print("cycle detect!")
            break
    else:
        print("no cycle!")

    print(parent)