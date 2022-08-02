from typing import List


class Union_Find:
    def __init__(self, length):
        self.length = length
        self.parent = [-1] * self.length

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: return False
        self.parent[root_x] = root_y
        return True

    def find(self, x):
        while self.parent[x] != -1:
            x = self.parent[x]
        return x


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        uf = Union_Find(m * n)
        count = 0
        table = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        res = []
        for x, y in positions:
            if (x, y) in table:
                res.append(count)
                continue
            count += 1
            table.add((x, y))

            for indent_x, indent_y in directions:
                new_x = x + indent_x
                new_y = y + indent_y
                if 0 <= new_x < m and 0 <= new_y < n:
                    if (new_x, new_y) in table:

                        if uf.union(x * n + y, new_x * n + new_y):
                            count -= 1
            res.append(count)

        return res


a = Solution().numIslands2(3, 3, [[0,0],[0,1],[1,2],[1,2]])
print(a)