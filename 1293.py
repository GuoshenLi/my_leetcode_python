from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        queue.append((0, 0, k, 0))
        visited = {(0, 0, k)}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for _ in range(len(queue)):
                x, y, rest, path_length = queue.popleft()
                if x == m - 1 and y == n - 1: return path_length
                for indent_x, indent_y in directions:
                    new_x = x + indent_x
                    new_y = y + indent_y

                    if 0 <= new_x < m and 0 <= new_y < n:
                        if grid[new_x][new_y] == 0 and (new_x, new_y, rest) not in visited:
                            queue.append((new_x, new_y, rest, path_length + 1))
                            visited.add((new_x, new_y, rest))

                        if grid[new_x][new_y] == 1 and rest > 0 and (new_x, new_y, rest - 1) not in visited:
                            queue.append((new_x, new_y, rest - 1, path_length + 1))
                            visited.add((new_x, new_y, rest - 1))

        return -1
