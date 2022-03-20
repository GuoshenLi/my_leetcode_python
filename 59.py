class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        left, right, top, buttom = 0, n - 1, 0, n - 1
        total_num = n ** 2
        num = 1
        matrix = [[0 for i in range(n)] for j in range(n)]

        while num <= total_num:
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1

            top += 1

            for i in range(top, buttom + 1):
                matrix[i][right] = num
                num += 1

            right -= 1

            for i in range(right, left - 1, -1):
                matrix[buttom][i] = num
                num += 1

            buttom -= 1

            for i in range(buttom, top - 1, -1):
                matrix[i][left] = num
                num += 1

            left += 1

        return matrix