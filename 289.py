# 用额外的空间
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        new_board = [[0 for _ in range(cols)] for _ in range(rows)]
        # 只能这么循环去写！千万不能用[[0] * cols] * rows

        x = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8 pos
        y = [-1, 0, 1, -1, 1, -1, 0, 1]  # 8 pos
        for i in range(rows):
            for j in range(cols):
                count = 0
                for x_, y_ in zip(x, y):
                    if 0 <= i + x_ <= rows - 1 and 0 <= j + y_ <= cols - 1 and board[i + x_][j + y_] == 1:
                        count += 1

                if board[i][j] == 1:
                    if count < 2:
                        new_board[i][j] = 0
                    elif count == 2 or count == 3:
                        new_board[i][j] = 1
                    elif count > 3:
                        new_board[i][j] = 0

                else:
                    if count == 3:
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = 0

        board[:] = new_board

# 原地搞定
# 用2记录原来死现在活
# 用-1记录原来活现在死
# 0 原来死现在也死
# 1 原来活现在也活


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 0 原来死亡 现在死亡
        # 1 原来存活 现在存活
        # -1 原来存活 现在死亡
        # 2 原来死亡 现在存活

        m = len(board)
        n = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(m):
            for j in range(n):

                count = 0
                for indent_x, indent_y in directions:
                    new_x = i + indent_x
                    new_y = j + indent_y

                    if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and abs(board[new_x][new_y]) == 1:
                        count += 1

                if abs(board[i][j]) == 1: # 包括原来存活的
                    if count < 2:
                        board[i][j] = -1
                    elif count == 2 or count == 3:
                        board[i][j] = 1
                    elif count > 3:
                        board[i][j] = -1

                elif board[i][j] == 0 or board[i][j] == 2: # 原来死亡的所有情况
                    if count == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 0




        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
