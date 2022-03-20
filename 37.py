# 暴力回溯 通过
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Rboard = len(board)
        Cboard = len(board[0])
        def isValid(row, col, val, board):
            for i in range(9):
                if board[row][i] == val or board[i][col] == val:
                    return False
            startRow = row // 3 * 3
            startCol = col // 3 * 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == val:
                        return False

            return True

        def backtracking(board):
            for i in range(Rboard):
                for j in range(Cboard):
                    if board[i][j] != '.':
                        continue
                    for k in range(1, 10):
                        if isValid(i, j, str(k), board):
                            board[i][j] = str(k)
                            if backtracking(board):
                                return True
                            board[i][j] = '.'
                    return False
            return True

        backtracking(board)


# 按行填充
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        line_used = [[False] * 10 for _ in range(9)]
        column_used = [[False] * 10 for _ in range(9)]
        block_used = [[[False] * 10 for _a in range(3)] for _b in range(3)]

        # line (9 * 10)
        # column (9 * 10)
        # block (3 * 3 * 10)

        # 初始化三个数组

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    line_used[i][num] = True
                    column_used[j][num] = True
                    block_used[i // 3][j // 3][num] = True

        self.dfs(board, line_used, column_used, block_used, 0, 0)

    def dfs(self, board, line_used, column_used, block_used, row, col):
        if col == 9:
            row += 1
            col = 0
            if row == 9:
                return True

        if board[row][col] == '.':
            for num in range(1, 10):
                can_use = not (line_used[row][num] or column_used[col][num] or block_used[row // 3][col // 3][num])

                if can_use:
                    line_used[row][num] = True
                    column_used[col][num] = True
                    block_used[row // 3][col // 3][num] = True
                    board[row][col] = str(num)

                    if self.dfs(board, line_used, column_used, block_used, row, col + 1):
                        return True

                    board[row][col] = '.'
                    line_used[row][num] = False
                    column_used[col][num] = False
                    block_used[row // 3][col // 3][num] = False

            return False

        else:
            return self.dfs(board, line_used, column_used, block_used, row, col + 1)


# 按行填充
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        block_set = [[set() for i in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_set[i].add(int(board[i][j]))
                    col_set[j].add(int(board[i][j]))
                    block_set[i // 3][j // 3].add(int(board[i][j]))

        def dfs(row, col):
            if col == 9:
                row += 1
                col = 0
                if row == 9:
                    return True

            if board[row][col] == '.':
                for num in range(1, 10):
                    if num in row_set[row] or num in col_set[col] or num in block_set[row // 3][col // 3]:
                        continue

                    row_set[row].add(num)
                    col_set[col].add(num)
                    block_set[row // 3][col // 3].add(num)
                    board[row][col] = str(num)

                    if dfs(row, col + 1): return True

                    row_set[row].remove(num)
                    col_set[col].remove(num)
                    block_set[row // 3][col // 3].remove(num)
                    board[row][col] = "."

                return False
            else:
                return dfs(row, col + 1)


        dfs(0, 0)




Solution().solveSudoku(board = [["5","3",".",".","7",".",".",".","."],
                                ["6",".",".","1","9","5",".",".","."],
                                [".","9","8",".",".",".",".","6","."],
                                ["8",".",".",".","6",".",".",".","3"],
                                ["4",".",".","8",".","3",".",".","1"],
                                ["7",".",".",".","2",".",".",".","6"],
                                [".","6",".",".",".",".","2","8","."],
                                [".",".",".","4","1","9",".",".","5"],
                                [".",".",".",".","8",".",".","7","9"]])