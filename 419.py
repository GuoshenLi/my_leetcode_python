class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        m = len(board)
        n = len(board[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count += 1

                    row = i
                    col = j + 1
                    while col < n and board[row][col] == 'X':
                        board[row][col] = '.'
                        col += 1

                    row = i + 1
                    col = j
                    while row < m and board[row][col] == 'X':
                        board[row][col] = '.'
                        row += 1

        return count