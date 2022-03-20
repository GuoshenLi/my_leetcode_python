from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        if all(True if grid[i][j] == 1 else False for i in range(m) for j in range(n)): return -1
        if all(True if grid[i][j] == 0 else False for i in range(m) for j in range(n)): return -1

        queue = deque()
        visited = set()
        max_dis = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited.add((i, j))

        while queue:
            x, y, level = queue.popleft()
            max_dis = max(max_dis, level)
            for indent_x, indent_y in directions:
                new_x = indent_x + x
                new_y = indent_y + y

                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, level + 1))
                    visited.add((new_x, new_y))

        return max_dis

