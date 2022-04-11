class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = 0
        while queue:
            x, y, step = queue.popleft()
            res = max(res, step)
            for indent_x, indent_y in directions:
                new_x = x + indent_x
                new_y = y + indent_y
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                    queue.append((new_x, new_y, step + 1))
                    grid[new_x][new_y] = 2


        return res if all(grid[i][j] == 2 for i in range(m) for j in range(n) if grid[i][j] != 0) else -1

