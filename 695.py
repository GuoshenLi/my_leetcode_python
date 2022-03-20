from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        global_max = 0
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


        def dfs(x, y):

            grid[x][y] = 0
            res = 1

            for indent_x, indent_y in directions:
                new_x = x + indent_x
                new_y = y + indent_y
                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and grid[new_x][new_y] == 1:
                    res += dfs(new_x, new_y)

            return res


        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))


        return res