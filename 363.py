from typing import List
# 暴力 24 / 39
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        self.pre_sum = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = self.pre_sum[i][j - 1] + self.pre_sum[i - 1][j] - self.pre_sum[i - 1][j - 1] + \
                                     matrix[i - 1][j - 1]
        print(self.pre_sum)
        res = float('-inf')
        for row1 in range(m):
            for row2 in range(row1 + 1, m):
                for col1 in range(n):
                    for col2 in range(col1 + 1, n):
                        # 从row1 到 row2 col1 到col2所形成的区域总和
                        tmp = self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row1][col2 + 1] - self.pre_sum[row2 + 1][
                            col1] + self.pre_sum[row1][col1]

                        if tmp <= k:
                            res = max(res, tmp)

        return res



# 25 / 39
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        self.pre_sum = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = self.pre_sum[i][j - 1] + self.pre_sum[i - 1][j] - self.pre_sum[i - 1][j - 1] + \
                                     matrix[i - 1][j - 1]
        print(self.pre_sum)
        res = float('-inf')

        for row1 in range(m + 1):
            for row2 in range(row1 + 1, m + 1):
                for col1 in range(n + 1):
                    for col2 in range(col1 + 1, n + 1):
                        # 从[row1, row2) [col1, col2) 所形成的区域总和
                        # 开区间
                        tmp = self.pre_sum[row2][col2] - self.pre_sum[row1][col2] - self.pre_sum[row2][
                            col1] + self.pre_sum[row1][col1]

                        if tmp <= k:
                            res = max(res, tmp)

        return res





from sortedcontainers import SortedList
# 简化版：
# 一维数组中和不超过k的连续子数组的最大和

class Solution:
    def maxSumSubmatrix(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        res = float('-inf')
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        # 暴力解法
        # for i in range(n + 1):
        #     for j in range(i + 1, n + 1):
        #         if pre_sum[j] - pre_sum[i] <= k:
        #             res = max(res, pre_sum[j] - pre_sum[i])

        # 同样考虑的问题就是如何才能够枚举完所有的区间和
        # 区间[i, j) i < j, 的和为pre_sum[j] - pre_sum[i]
        # sum[i, j) <= k 也就是 pre_sum[j] - pre_sum[i] <= k
        # 也就是固定j 然后 (pre_sum[j] - k)(常量) <= pre_sum[i]
        # 找满足条件的最小的pre_sum[i] 即可
        # 而i < j 因此 遍历j的时候i总比j要落后一个单位 因此可以保证正确并且能取完所有区间可能性

        # 这一点很关键
        left_presum = SortedList([0])
        for j in range(1, n + 1):
            right_presum = pre_sum[j]
            idx = left_presum.bisect_left(right_presum - k)
            # 确保能找到一个小于等于right - k的
            if idx < len(left_presum):
                cur = right_presum - left_presum[idx]
                res = max(res, cur)

            left_presum.add(right_presum)

        return res



from sortedcontainers import SortedList
#  也是暴力的一种
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        res = float("-inf")
        m, n = len(matrix), len(matrix[0])

        pre_sum = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] - pre_sum[i - 1][j - 1] + matrix[i - 1][j - 1]

        # 参考一维度的
        # 固定上下 然后就变成一维的了
        # 上下之间形成一个大矩阵 看成一维的
        # 枚举所有上下边界
        # 用二分查找搜索最大值

        for upper in range(m + 1):
            for button in range(upper + 1, m + 1):

                # 这一点很关键
                left_presum = SortedList([0])
                for j in range(1, n + 1):
                    right_presum = pre_sum[button][j] - pre_sum[upper][j]
                    idx = left_presum.bisect_left(right_presum - k)

                    if idx < len(left_presum):
                        cur = right_presum - left_presum[idx]
                        res = max(res, cur)

                    left_presum.add(right_presum)

        return res

# 如果行数大于列数 反过来一下下。
from sortedcontainers import SortedList
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = float("-inf")
        pre_sum = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_sum[i][j] = pre_sum[i - 1][j] + pre_sum[i][j - 1] + matrix[i - 1][j - 1] - pre_sum[i - 1][j - 1]

        for left in range(n + 1):
            for right in range(left + 1, n + 1):
                upper_presum = SortedList([0])
                '''
                    pre_sum[j] - pre_sum[i] <= k
                    pre_sum[i] >= pre_sum[j] - k
                    在有序数组中找第一个大于pre_sum[j] - k的pre_sum[i]
                '''
                for j in range(1, m + 1):
                    bottom_presum = pre_sum[j][right] - pre_sum[j][left]
                    idx = upper_presum.bisect_left(bottom_presum - k)
                    if idx < len(upper_presum):
                        res = max(res, bottom_presum - upper_presum[idx])
                    upper_presum.add(bottom_presum)

        return res


