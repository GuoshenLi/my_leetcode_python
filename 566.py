from typing import List
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])

        if row * col != r * c:
            return nums

        res = [[0] * c for _ in range(r)]

        count = 0

        for i in range(r):
            for j in range(c):
                res[i][j] = nums[count // col][count % col]
                count += 1

        return res



class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])

        if r * c != m * n: return mat

        res = [[None] * c for _ in range(r)]

        index = 0
        for i in range(m):
            for j in range(n):
                res[index // c][index % c] = mat[i][j]
                index += 1

        return res


print(Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))