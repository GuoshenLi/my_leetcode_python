class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix_line = [set() for i in range(9)]
        matrix_column = [set() for i in range(9)]
        matrix_area = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                item = board[i][j]

                if item != '.':
                    if item not in matrix_line[i] and item not in matrix_column[j] and item not in matrix_area[i // 3][j // 3]:
                        matrix_line[i].add(item)
                        matrix_column[j].add(item)
                        matrix_area[i // 3][j // 3].add(item)
                    else:
                        return False
        return True