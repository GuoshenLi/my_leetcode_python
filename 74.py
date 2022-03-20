class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                return self.binary_search(matrix[i], target)
        return False

    def binary_search(self, array, target):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix[0]: return False

        # 选择右上角或者左下角
        row, col = 0, len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if matrix[row][col] < target:
                row += 1

            elif matrix[row][col] > target:
                col -= 1

            else:
                return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        # 两次二分查找
        # 找到target所在行，找最后一个小于等于

        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0]: return False

        left, right = 0, m - 1

        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][0] <= target:
                left = mid
            else:
                right = mid - 1

        target_row = left

        # 知道行以后再去找哪一列

        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
