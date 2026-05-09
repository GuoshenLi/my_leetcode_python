class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)

        def search(up, down):
            middle_row = (up + down) // 2
            middle_max = max(mat[middle_row])
            j = mat[middle_row].index(middle_max)
            if up == down:
                return [middle_row, j]

            if middle_row - 1 >= 0 and mat[middle_row][j] < mat[middle_row - 1][j]:
                return search(up, middle_row - 1)

            elif middle_row + 1 < m and mat[middle_row][j] < mat[middle_row + 1][j]:
                return search(middle_row + 1, down)

            else:
                return [middle_row, j]

        return search(0, m - 1)



