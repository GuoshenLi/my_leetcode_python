# 外面补0

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        c = 0
        m, n = len(grid), len(grid[0])
        new_grid = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m):
            for j in range(n):
                new_grid[i + 1][j + 1] = grid[i][j]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if new_grid[i][j] == 1:
                    c += [new_grid[i - 1][j], new_grid[i + 1][j], new_grid[i][j - 1], new_grid[i][j + 1]].count(0)
        return c