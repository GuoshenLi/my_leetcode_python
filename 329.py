# 这个题目其实很简单！
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        memo = {}
        def dfs(x, y):
            if (x, y) in memo: return memo[(x, y)]
            length = 1

            for indent_x, indent_y in directions:
                new_x = indent_x + x
                new_y = indent_y + y
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] > matrix[x][y]:
                    length = max(length, dfs(new_x, new_y) + 1)

            memo[(x, y)] = length
            return length




        max_len = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                max_len = max(max_len, dfs(i, j))

        return max_len