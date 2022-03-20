# 二维平面上的回溯
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        m = len(board)
        n = len(board[0])
        length = len(word)
        vidited = [[False] * n for i in range(m)]

        def dfs(i, j, index):
            if index == length - 1:
                return board[i][j] == word[index]
            elif board[i][j] != word[index]:
                return False
            # 等于
            vidited[i][j] = True
            for indent_x, indent_y in direction:
                new_x = i + indent_x
                new_y = j + indent_y

                if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and vidited[new_x][new_y] == False:
                    if dfs(new_x, new_y, index + 1): return True

            vidited[i][j] = False
            return False


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False