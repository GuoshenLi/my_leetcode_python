from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n

        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                this = 2

                # 这两个点确定直线的斜率
                # 这一有可能斜率不存在！
                if points[i][0] == points[j][0]:
                    # 斜率不存在
                    unexist = True
                else:
                    # 斜率存在
                    unexist = False
                    tangent = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    # 妈的还复杂了 可以直接避开除法。
                for k in range(n):
                    if k != i and k != j:
                        if unexist:
                            # 如果开始两个点的斜率不存在，那么只用判断
                            # 第三个点的横坐标一不一样

                            if points[i][0] == points[k][0]:
                                this += 1
                        else:
                            # 如果两个点斜率存在，那么第三个点也要斜率存在并且一样 
                            # 如果第三个点斜率不存在，不可能构成直线。。 细品

                            if points[i][0] == points[k][0]:
                                continue
                            tangent_new = (points[i][1] - points[k][1]) / (points[i][0] - points[k][0])
                            if tangent == tangent_new:
                                this += 1


                res = max(res, this)


        return res

# 简化版的暴力
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2: return n

        res = 0
        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n):
                p2 = points[j]
                count = 2
                for k in range(j + 1, n):
                    p3 = points[k]

                    # 斜率相等
                    # (p2[1] - p1[1]) / (p2[0] - p1[0]) = (p3[1] - p2[1]) / (p3[0] - p2[0])
                    # 换成乘法 这样可以避免分类讨论

                    if  (p2[1] - p1[1]) * (p3[0] - p2[0]) == (p2[0] - p1[0]) * (p3[1] - p2[1]):
                        count += 1

                res = max(res, count)

        return res

from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n
        ans = 0

        for i in range(len(points) - 1):
            duplicate = 1
            table = defaultdict(int)
            for j in range(i + 1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicate += 1
                else:
                    table[dy / dx if dx else float('+inf')] += 1
            ans = max(ans, max(table.values()) + duplicate)
        return ans