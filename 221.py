import heapq
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # 以dp[i][j]为终点能够变成多大的正方形的边长
        maxSide = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]

        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                maxSide = 1

        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                maxSide = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                    maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide