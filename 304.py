# 一维前缀和
from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.presum[i][j + 1] = self.presum[i][j] + matrix[i][j]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            sum += self.presum[i][col2 + 1] - self.presum[i][col1]
        return sum

# 二维前缀和
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix: return None

        M, N = len(matrix), len(matrix[0])

        self.preSum = [[0] * (N + 1) for _ in range(M + 1)] # 里面可以乘 外面不能乘 死背 2D 数组
        for i in range(M):
            for j in range(N):
                self.preSum[i + 1][j + 1] = self.preSum[i][j + 1] + self.preSum[i + 1][j]  - self.preSum[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row2 + 1][col1] - self.preSum[row1][col2 + 1] + self.preSum[row1][col1]









# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
print(obj.sumRegion(1,2,2,4))


