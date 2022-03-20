from typing import List
# 从两个大洋出发 逆流而上
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        if not matrix or len(matrix) == 0:
            return res

        directions = [[0,1], [0,-1], [1, 0], [-1,0]]

        m = len(matrix)
        n = len(matrix[0])

        canP = [[0] * n for _ in range(m)]
        canA = [[0] * n for _ in range(m)]

        def dfs(row, col, ocean):
            if not ocean[row][col]:
                ocean[row][col] = 1
                for direction in directions:
                    x = row + direction[0]
                    y = col + direction[1]
                    if x >= m or x < 0  or y >= n or y < 0 or matrix[x][y] < matrix[row][col]:
                        continue
                    dfs(x, y, ocean)

        for i in range(m):
            dfs(i, 0, canP)
            dfs(i, n-1, canA)

        for j in range(n):
            dfs(0, j, canP)
            dfs(m-1, j, canA)

        for i in range(m):
            for j in range(n):
                if canA[i][j] and canP[i][j]:
                    res.append([i,j])
        return res


# bfs
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        if m == 0 or n == 0: return []
        ocean_p = [[0] * n for i in range(m)]
        ocean_a = [[0] * n for i in range(m)]

        queue_p = deque()
        queue_a = deque()

        for i in range(m):
            queue_p.append((i, 0))
            queue_a.append((i, n - 1))

        for j in range(n):
            queue_p.append((0, j))
            queue_a.append((m - 1, j))

        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while queue_p:
            x, y = queue_p.popleft()
            ocean_p[x][y] = 1
            for indent_x, indent_y in direction:
                new_x = x + indent_x
                new_y = y + indent_y
                if 0 <= new_x < m and 0 <= new_y < n and ocean_p[new_x][new_y] == 0 and heights[new_x][new_y] >= \
                        heights[x][y]:
                    queue_p.append((new_x, new_y))

        while queue_a:
            x, y = queue_a.popleft()
            ocean_a[x][y] = 1
            for indent_x, indent_y in direction:
                new_x = x + indent_x
                new_y = y + indent_y
                if 0 <= new_x < m and 0 <= new_y < n and ocean_a[new_x][new_y] == 0 and heights[new_x][new_y] >= \
                        heights[x][y]:
                    queue_a.append((new_x, new_y))

        res = []
        for i in range(m):
            for j in range(n):
                if ocean_a[i][j] == 1 and ocean_p[i][j] == 1:
                    res.append([i, j])

        return res


print(Solution().pacificAtlantic(matrix=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))