from typing import List
import collections
# 1162一样
class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]

        # 初始化队列，将所有起始点加入
        for i in range(m):
            for j in range(n):

                queue = collections.deque([])
                visited = set()
                queue.append((i, j, 0))
                visited.add((i, j))
                while queue:
                    x, y, level = queue.popleft()
                    if matrix[x][y] == 0:
                        res[i][j] = level
                        break

                    for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                            queue.append((new_x, new_y, level + 1))
                            visited.add((new_x, new_y))

        return res




# 多源广度优先
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]  # 设定结果集
        # res 保存当前点与0的最近距离
        q = collections.deque()  # BFS 经典结果，设定一个 queue 来存储每个层次上的点
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:  # 将题目转换为 0 到其它点的距离
                    res[i][j] = 0  # 0到自身的距离为零
                    q.append([i, j, 0])  # 将找到的 0 放入队列
        while q:  # BFS 经典模板
            x, y, level = q.popleft()  # 取出某层上的点
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 加四个方向的偏置
                new_x = x + x_bias
                new_y = y + y_bias
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and res[new_x][new_y] == None:  # 判断扩展点有效性
                    res[new_x][new_y] = level + 1
                    q.append([new_x, new_y, level + 1])  # 将新扩展的点加入队列
        return res


# 根据上述思路，本题怎么做就很简单了：
# 首先把每个源点 0 入队，然后从各个 0 同时开始一圈一圈的向 1 扩散
#（每个 1 都是被离它最近的 0 扩散到的 ），扩散的时候可以设置 None 来记录距离（即扩散的层次）并同时标志是否访问过。
# 只要被访问过 就不会再访问了 因为已经有最短了
# 对于本题是可以直接修改原数组 res 来记录距离和标志是否访问的，这里要注意先把 matrix 数组中 1 的位置设置成 None
#（设成Integer.MAX_VALUE啦，m * n啦，10000啦都行，只要是个无效的距离值来标志这个位置的 1 没有被访问过就行辣~）




# 二维回溯 不能记忆化
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        res = [[0] * n for i in range(m)]
        visited = [[False] * n for i in range(m)]


        def dfs(x, y):

            if mat[x][y] == 1:
                min_dis = float('+inf')
                for indent_x, indent_y in directions:
                    new_x = x + indent_x
                    new_y = y + indent_y

                    if 0 <= new_x < m and 0 <= new_y < n and visited[new_x][new_y] == False:
                        visited[new_x][new_y] = True
                        min_dis = min(min_dis, dfs(new_x, new_y) + 1)
                        visited[new_x][new_y] = False

                return min_dis

            else:
                return 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    res[i][j] = dfs(i, j)

        return res
