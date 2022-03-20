# 暴力回溯 37 / 101
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        self.res = 0
        n = len(nums)

        def dfs(inedx, tmp):
            if len(tmp) >= 3:
                if self.check(tmp):
                    self.res += 1

            for i in range(inedx, n):
                tmp.append(nums[i])
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(0, [])
        return self.res

    def check(self, tmp):
        i = 2
        while i < len(tmp) and tmp[i] - tmp[i - 1] == tmp[i - 1] - tmp[i - 2]:
            i += 1

        return i == len(tmp)




# 动态规划
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        index_table = defaultdict(list)
        n = len(A)
        for i in range(n):
            index_table[A[i]].append(i)

        # 存每个数字的下标 有可能重复 因此list的元素可能不止一个

        dp = [[0] * n for i in range(n)]
        # dp[i][j] 以A[j] A[i]结尾的长度大于等于3的等差数列的个数
        res = 0
        for i in range(2, n):
            for j in range(i):
                # A[k], A[j], A[i]
                # 我们要找 A[i] - A[j] == A[j] - A[k]
                # 因此target为 2 * A[j] - A[i]
                target = 2 * A[j] - A[i]
                if target in index_table:
                    for k in index_table[target]:
                        if k < j:
                            dp[i][j] += (dp[j][k] + 1)

                res += dp[i][j]

        return res
