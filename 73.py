from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_loc = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_loc.append([i, j])

        for zero in zero_loc:
            row = zero[0]
            col = zero[1]

            for j in range(len(matrix[0])):
                matrix[row][j] = 0

            for i in range(len(matrix)):
                matrix[i][col] = 0

# 所在行和列的非零元素 设置成'set_zero'
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'set_zero'
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'set_zero'

                    for v in range(len(matrix[0])):
                        if matrix[i][v] != 0:
                            matrix[i][v] = 'set_zero'

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'set_zero':
                    matrix[i][j] = 0


###
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False

        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break

        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        #print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0

        print("finished!")

print(Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

