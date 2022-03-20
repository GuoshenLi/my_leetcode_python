# 广度优先搜索
# 把与边界相连接的 'O' 全部标记为 'A'
# 然后遍历board (1): 'X' 不变 (2):'A' 变为'O' (3): 'O'变为'X'
# 从四周开始扩散
from collections import deque
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        que = deque()
        for i in range(m):
            if board[i][0] == "O":
                que.append((i, 0))
            if board[i][n - 1] == "O":
                que.append((i, n - 1))

        for i in range(1, n - 1):
            if board[0][i] == "O":
                que.append((0, i))
            if board[m - 1][i] == "O":
                que.append((m - 1, i))

        while que:
            x, y = que.popleft()
            board[x][y] = "A"
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < m and 0 <= my < n and board[mx][my] == "O":
                    que.append((mx, my))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        m, n = len(board), len(board[0])
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(x, y):
            # 第一次进来要判断！！！
            if board[x][y] == 'O':
                board[x][y] = "A"
            else:
                return None

            for indent_x, indent_y in direction:
                new_x = indent_x + x
                new_y = indent_y + y
                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and board[new_x][new_y] == 'O':
                    dfs(new_x, new_y)

            return None

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(1, n - 1):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"



Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
