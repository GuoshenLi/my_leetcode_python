# 典型的记忆化递归
class Solution:
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        memo = {}
        moves = ((-1, -2), (-2, -1),(-2, 1), (-1, 2),(1, -2), (2, -1),(2, 1), (1, 2))
        def dfs(K, r, c):
            if K == 0:
                return 1
            if (K, r, c) in memo:
                return memo[(K, r, c)]

            p = 0
            for move in moves:
                new_r = r + move[0]
                new_c = c + move[1]
                if 0 <= new_r <= N - 1 and 0 <= new_c <= N - 1:
                    p += dfs(K-1, new_r, new_c)

            p /= 8.0
            memo[(K, r, c)] = p
            return p
        return dfs(K, r, c)




# 动态规划
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp[i][j][k]
        dp = [[[0 for i in range(k + 1)] for j in range(n)] for p in range(n)]
        moves = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2))

        dp[row][column][0] = 1

        for p in range(1, k + 1):
            for i in range(n):
                for j in range(n):

                    for direc in moves:
                        row_new = i + direc[0]
                        col_new = j + direc[1]
                        if 0 <= row_new < n and 0 <= col_new < n:
                            dp[i][j][p] += dp[row_new][col_new][p - 1] / 8.0

        res = 0

        for i in range(n):
            for j in range(n):
                res += dp[i][j][k]
        return res




