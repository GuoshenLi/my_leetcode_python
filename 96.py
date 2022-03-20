# 记忆化递归 肯定可以过 突破口 连续i个数字构造的树的个数是一样的。
# 1234 和2345构造的BST个数相同。
# 动态规划



class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]



class Solution:
    def numTrees(self, n: int) -> int:
        self.table = {}
        def dfs(n):
            if n == 0 or n == 1: return 1

            if n in self.table: return self.table[n]

            sum_ = 0
            for j in range(0, n):
                sum_ += dfs(j) * dfs(n - j - 1)
            self.table[n] = sum_
            return self.table[n]


        return dfs(n)