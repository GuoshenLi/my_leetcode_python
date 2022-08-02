class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = set()
        m = len(grid)
        n = len(grid[0])

        directions = [(-1, 0, "0"), (1, 0, "1"), (0, -1, "2"), (0, 1, "3")]

        def dfs(x, y):
            grid[x][y] = 0

            for indent_x, indent_y, flag in directions:
                new_x = x + indent_x
                new_y = y + indent_y

                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    self.path += "+" + flag
                    dfs(new_x, new_y)
                    self.path += "-" + flag

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.path = "begin"
                    dfs(i, j)
                    res.add(self.path)

        print(res)
        return len(res)