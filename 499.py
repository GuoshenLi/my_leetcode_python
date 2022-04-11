# modified dijstra 算法
import heapq
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])
        directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
        def roll(x, y, indent_x, indent_y):

            while 0 <= x + indent_x < m and 0 <= y + indent_y < n and maze[x + indent_x][y + indent_y] == 0:

                x += indent_x
                y += indent_y

                if [x, y] == hole:
                    break

            return x, y

        distance = [[float('+inf')] * n for i in range(m)]
        distance[ball[0]][ball[1]] = 0
        heap = [[0, "", ball[0], ball[1]]]
        visited = set()

        while heap:
            dis, string, x, y = heapq.heappop(heap)
            if (x, y) in visited: continue
            if x == hole[0] and y == hole[1]: return string

            visited.add((x, y))
            for indent_x, indent_y, char in directions:

                new_x, new_y = roll(x, y, indent_x, indent_y)

                steps = abs(new_x - x) + abs(new_y - y)

                if dis + steps <= distance[new_x][new_y]:
                    # 一定要 <=, 因为可能有多个最短路径,但是要比较字典序,所以要=
                    distance[new_x][new_y] = dis + steps
                    heapq.heappush(heap, [distance[new_x][new_y], string + char, new_x, new_y])


        return "impossible"
