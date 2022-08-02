class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j, island):
            for x, y in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                ni, nj = i + x, j + y
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj) not in island:
                    grid[ni][nj] = 0
                    island.append((ni, nj))
                    dfs(ni, nj, island)
            return island

        def shape(island):
            rotate = [sorted([(x, y) for x, y in island]),
                      sorted([(-x, y) for x, y in island]),
                      sorted([(x, -y) for x, y in island]),
                      sorted([(y, -x) for x, y in island]),
                      sorted([(-x, -y) for x, y in island]),
                      sorted([(-y, x) for x, y in island]),
                      sorted([(y, x) for x, y in island]),
                      sorted([(-y, -x) for x, y in island])
                      ]
            shapes = []
            for i in rotate:
                min_r, min_c = i[0][0], i[0][1]
                cur_shape = [(x - min_r, y - min_c) for x, y in i]
                shapes.append(tuple(cur_shape))
            return shapes

        count = 0
        total_island = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_island = sorted(dfs(i, j, [(i, j)]))
                    min_r, min_c = cur_island[0][0], cur_island[0][1]
                    tmp = tuple([(x - min_r, y - min_c) for x, y in cur_island])
                    if tmp not in total_island:
                        count += 1
                        shapes = shape(cur_island)
                        total_island |= set(shapes)
        return count




print(Solution().numDistinctIslands2(grid=[[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]))