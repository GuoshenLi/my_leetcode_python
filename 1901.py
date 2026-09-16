class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)

        def dfs(mat, up, down):

            mid_row = (up + down) // 2
            mid_max = max(mat[mid_row])
            j = mat[mid_row].index(mid_max)
            if up == down:
                return [mid_row, j]

            if mid_row - 1 >= 0 and mat[mid_row][j] <= mat[mid_row - 1][j]:
                return dfs(mat, up, mid_row - 1)

            elif mid_row + 1 <= m - 1 and mat[mid_row][j] <= mat[mid_row + 1][j]:
                return dfs(mat, mid_row + 1, down)

            else:
                return [mid_row, j]

        return dfs(mat, 0, m - 1)