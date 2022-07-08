from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        heights = [0 for _ in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
            res = max(res, self.maxrectangle(heights))

        return res

    def maxrectangle(self, heights):
        ans = 0
        heights = [0] + heights + [0]
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                ans = max(ans, heights[cur] * (i - stack[-1] - 1))
            stack.append(i)
        return ans