# modified dijstra
import heapq
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

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
            if x == destination[0] and y == destination[1]: return True
            if (x, y) in visited: continue

            visited.add((x, y))
            for indent_x, indent_y in directions:
                new_x, new_y = roll(x, y, indent_x, indent_y)
                steps = abs(new_x - x) + abs(new_y - y)

                if dis + steps < distance[new_x][new_y]:
                    distance[new_x][new_y] = dis + steps
                    heapq.heappush(heap, (distance[new_x][new_y], new_x, new_y))


        return False



from collections import deque
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque()
        queue.append((start[0], start[1]))
        visited[start[0]][start[1]] = True
        while queue:
            x, y = queue.popleft()
            if [x, y] == destination:
                return True
            for indent_x, indent_y in ((0,1), (1,0), (0,-1), (-1,0)):
                new_x = x + indent_x
                new_y = y + indent_y
                while 0 <= new_x < m and 0<= new_y < n and maze[new_x][new_y] == 0:
                    new_x += indent_x
                    new_y += indent_y
                new_x -= indent_x        #碰壁了，退后一步
                new_y -= indent_y        #碰壁了，退后一步
                if visited[new_x][new_y] == False:    #下一步的起点
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))

        return False

