import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        水从高处往低处流，某个位置储水量取决于四周最低高度，从最外层向里层包抄，用小顶堆动态找到未访问位置最小的高度
        """

        if not heightMap: return 0

        ans = 0
        heap = []
        visited = set()
        row = len(heightMap)
        col = len(heightMap[0])

        # 将最外层放入小顶堆
        # 第一行和最后一行
        for j in range(col):
            # 将该位置的高度、横纵坐标插入堆
            heapq.heappush(heap, [heightMap[0][j], 0, j])
            heapq.heappush(heap, [heightMap[row - 1][j], row - 1, j])
            visited.add((0, j))
            visited.add((row - 1, j))

        # 第一列和最后一列
        for i in range(1, row - 1):
            heapq.heappush(heap, [heightMap[i][0], i, 0])
            heapq.heappush(heap, [heightMap[i][col - 1], i, col - 1])
            visited.add((i, 0))
            visited.add((i, col - 1))

        while heap:
            h, i, j = heapq.heappop(heap)
            # 之前最低高度的四周已经探索过了，所以要更新为次低高度开始探索
            # 从堆顶元素出发，探索四周储水位置
            for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                tmp_x = x + i
                tmp_y = y + j
                # 是否到达边界
                if tmp_x < 0 or tmp_y < 0 or tmp_x >= row or tmp_y >= col or (tmp_x, tmp_y) in visited:
                    continue

                if heightMap[tmp_x][tmp_y] < h:
                    ans += h - heightMap[tmp_x][tmp_y]

                visited.add((tmp_x, tmp_y))

                # 更新一下下高度 其实就是一种扩散
                heapq.heappush(heap, [max(h, heightMap[tmp_x][tmp_y]), tmp_x, tmp_y])

        return ans



