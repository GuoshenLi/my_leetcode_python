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


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        total_number = n ** 2
        count = 1
        left, right, up, down = 0, n - 1, 0, n - 1
        while True:
            for j in range(left, right + 1):
                matrix[up][j] = count
                count += 1
            up += 1
            if up > down: return matrix
            for i in range(up, down + 1):
                matrix[i][right] = count
                count += 1

            right -= 1
            if right < left: return matrix
            for j in range(right, left - 1, -1):
                matrix[down][j] = count
                count += 1

            down -= 1
            if up > down: return matrix
            for i in range(down, up - 1, -1):
                matrix[i][left] = count
                count += 1

            left += 1
            if left > right: return matrix

