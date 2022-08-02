class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        nodes = [None] * (N * N)
        for i in range(N):
            for j in range(N):
                nodes[grid[i][j]] = (i, j)
        dsu = DSU(N * N)
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i, node in enumerate(nodes):
            x, y = node[0], node[1]
            for dir in dirs:
                newx = x + dir[0]
                newy = y + dir[1]
                if newx >= 0 and newx < N and newy >= 0 and newy < N and grid[newx][newy] < i:
                    dsu.union(x * N + y, newx * N + newy)
            if dsu.connected(0, N * N - 1):
                return i
        return 0


class DSU:
    def __init__(self, size):
        self.par = list(range(size))

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)



print(Solution().swimInWater(grid=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))