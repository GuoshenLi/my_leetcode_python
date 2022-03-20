class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        m = len(board)
        n = len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def dfs(x, y):
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return None

            elif board[x][y] == 'E':
                count = 0
                for indent_x, indent_y in directions:
                    new_x = x + indent_x
                    new_y = y + indent_y

                    if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and board[new_x][new_y] == 'M':
                        count += 1

                if count == 0:
                    board[x][y] = 'B'
                    for indent_x, indent_y in directions:
                        new_x = x + indent_x
                        new_y = y + indent_y

                        if 0 <= new_x <= m - 1 and 0 <= new_y <= n - 1 and board[new_x][new_y] == 'E':
                            dfs(new_x, new_y)

                else:
                    board[x][y] = str(count)





        dfs(click[0], click[1])
        return board


