class Solution:
    def totalNQueens(self, n: int) -> int:


        col_set, pie_set, na_set = set(), set(), set()

        def dfs(row):
            if row == n:
                return 1

            res = 0

            for col in range(n):
                if col in col_set or row - col in pie_set or row + col in na_set:
                    continue

                col_set.add(col)
                pie_set.add(row - col)
                na_set.add(row + col)

                res += dfs(row + 1)
                col_set.remove(col)
                pie_set.remove(row - col)
                na_set.remove(row + col)



            return res



        return dfs(0)