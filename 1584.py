# 最小生成树 prim 算法 模版
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #
        in_MST = [False] * n
        min_dis = [float('+inf')] * n
        dis_graph = [[float('+inf')] * n for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dis_graph[i][j] = w
                dis_graph[j][i] = w

        # 从结点0开始
        # 初始化
        in_MST[0] = True
        res = 0
        for i in range(1, n):
            min_dis[i] = dis_graph[0][i]

        for _ in range(1, n):
            min_val = float('+inf')
            for j in range(n):
                if not in_MST[j] and min_dis[j] < min_val:
                    min_index = j
                    min_val = min_dis[j]

            res += min_val
            in_MST[min_index] = True

            for j in range(n):
                if not in_MST[j] and dis_graph[j][min_index] < min_dis[j]:
                    min_dis[j] = dis_graph[j][min_index]


        return res
