# modified dijstra
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def roll(x, y, indent_x, indent_y):
            while 0 <= x + indent_x < m and 0 <= y + indent_y < n and maze[x + indent_x][y + indent_y] == 0:
                x += indent_x
                y += indent_y

            return x, y

        distance = [[float('+inf')] * n for i in range(m)]
        distance[start[0]][start[1]] = 0

        heap = [[0, start[0], start[1]]]
        visited = set()
        while heap:
            dis, x, y = heapq.heappop(heap)
            if (x, y) in visited: continue
            if x == destination[0] and y == destination[1]: return dis
            visited.add((x, y))

            for indent_x, indent_y in directions:
                new_x, new_y = roll(x, y, indent_x, indent_y)
                steps = abs(new_x - x) + abs(new_y - y)

                if dis + steps < distance[new_x][new_y]:
                    distance[new_x][new_y] = dis + steps
                    heapq.heappush(heap, (distance[new_x][new_y], new_x, new_y))


        return -1