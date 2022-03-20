class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        res = []
        col_set, diag1_set, diag2_set = set(), set(), set()

        def dfs(row):
            if row == n:
                res.append(list(map(''.join, board)))
                return None

            for col in range(n):
                if col in col_set or row - col in diag1_set or row + col in diag2_set:
                    continue


                board[row][col] = 'Q'
                col_set.add(col)
                diag1_set.add(row - col)
                diag2_set.add(row + col)

                dfs(row + 1)
                board[row][col] = '.'
                col_set.remove(col)
                diag1_set.remove(row - col)
                diag2_set.remove(row + col)

        board = [['.'] * n for i in range(n)]
        dfs(0)

        return res
