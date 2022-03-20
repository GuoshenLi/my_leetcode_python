# 单调栈，死背。
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        heights = [0] + heights + [0]
        stack = []
        res = 0


        # 其实就是求每一根柱子向右延伸能够组成多大的矩形
        # 若极端情况， 全部柱子高度相等，则执行到i=右边哨兵时候强迫所有节点出栈，则中间过程\
        # 会出错， 但结果不会出错，执行到最左边的柱子不会出错（结果）即可。
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                # 加上while stack非空 其实可以不用，但是为了统一代码
                cur = stack.pop() # 当前柱子位置
                cur_height = heights[cur] # 当前柱子高度
                max_width = i - stack[-1] - 1
                res = max(res, cur_height * max_width)

            stack.append(i)

        return res



# 暴力法
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力解法
        if not heights: return 0
        n = len(heights)

        res = 0

        for i in range(n):

            left = i - 1
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1

            right = i + 1
            while right <= n - 1 and heights[right] >= heights[i]:
                right += 1

            left += 1
            right -= 1
            res = max(res, (right - left + 1) * heights[i])

        return res