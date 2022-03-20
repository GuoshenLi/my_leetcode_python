from collections import defaultdict
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 1,总面积等于小块的面积和
        # 2,除大矩形4个顶点外其它点都出现偶数(2或4)次

        # 自己举个例子，慢慢理解

        min_left, min_bottom = float('+inf'), float('+inf')
        max_right, max_upper = float('-inf'), float('-inf')
        table = defaultdict(int)
        s = 0
        for x1, y1, x2, y2 in rectangles:
            min_left = min(min_left, x1)
            min_bottom = min(min_bottom, y1)

            max_right = max(max_right, x2)
            max_upper = max(max_upper, y2)

            # 每个矩形4个点都加进去

            table[(x1, y1)] += 1
            table[(x2, y2)] += 1
            table[(x1, y2)] += 1
            table[(x2, y1)] += 1
            s += ((x2 - x1) * (y2 - y1))

        table[(min_left, min_bottom)] += 1
        table[(max_right, max_upper)] += 1
        table[(min_left, max_upper)] += 1
        table[(max_right, min_bottom)] += 1
        # 把最大矩形4个点都加进去

        if s != (max_right - min_left) * (max_upper - min_bottom):
            return False

        for k, v in table.items():
            if v % 2 != 0:
                return False
        return True

