from collections import defaultdict
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        table = {}
        n = len(accounts)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email not in table:
                    table[email] = i
                else:
                    uf.union(i, table[email])  # 同一个人

        temp = defaultdict(list)
        for k, v in table.items():
            temp[uf.find(v)].append(k)

        res = []
        for k, v in temp.items():
            res.append([accounts[k][0]] + sorted(v))
        return res










