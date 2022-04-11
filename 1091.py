from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for i in range(m)]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        res = 0

        queue = deque()
        queue.append((0, 0, 1))
        visited[0][0] = True

        while queue:
            x, y, step = queue.popleft()
            if x == n - 1 and y == n - 1:
                return step
            for indent_x, indent_y in directions:
                new_x = indent_x + x
                new_y = indent_y + y

                if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == False and grid[new_x][new_y] == 0:
                    queue.append((new_x, new_y, step + 1))
                    visited[new_x][new_y] = True

        return -1
