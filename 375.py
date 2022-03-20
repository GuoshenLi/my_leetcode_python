# 玩游戏 全都用记忆化递归
# 首先，我们需要意识到我们在范围 (1, n) 中猜数字的时候，需要考虑最坏情况下的代价。
# 也就是说要算每次都猜错的情况下的总体最大开销。

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}

        def dfs(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left >= right:
                return 0
            #用min表示在选1，2，3，。。n中选最小的费用（满足题目至少）    用max保证选i这个操作，最坏的情况也能玩得下去
            memo[(left, right)] = min(i + max(dfs(left, i - 1), dfs(i + 1, right)) for i in range(left, right + 1))
            # 枚举所有可能的猜到的数字（分割节点）,每个分割节点都要考虑最坏的情况，综合起来选最小的代价，才满足题目至少，细品！
            return memo[(left, right)]

        return dfs(1, n)
