# 对于值为'1'的点，启动深度优先搜索，把遍历到的点全部变成'0'
# 遍历整个数组，启动深度优先搜索的次数就是岛屿的数量
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(grid, x, y):
            grid[x][y] = '0'
            for indent_x, indent_y in direction:
                new_x = indent_x + x
                new_y = indent_y + y

                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and grid[new_x][new_y] == '1':
                    dfs(grid, new_x, new_y)

        m = len(grid)
        n = len(grid[0])
        num_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    num_island += 1

        return num_island


# 宽度优先搜索
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":

                    grid[r][c] = "0"
                    queue = deque()
                    queue.append((r, c))
                    while queue:
                        row, col = queue.popleft()
                        for x, y in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                                queue.append((x, y))
                                grid[x][y] = "0"

                    num_islands += 1
        return num_islands

