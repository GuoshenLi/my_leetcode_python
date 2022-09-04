from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        if stones[1] > 1: return False

        # 从start开始跳，通过跳了k步来到start
        @lru_cache(None)
        def dfs(start, k):
            if start == n - 1: return True

            for i in range(start + 1, n):
                gap = stones[i] - stones[start]
                if gap <= k + 1 and gap >= k - 1:
                    if dfs(i, gap):
                        return True

            return False

        return dfs(1, 1)


# 动态规划
from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        set_stones = set(stones)

        dp = defaultdict(set)
        dp[0].add(0)

        # dp[i] 存储的是到达位置为i的石头，前一步所有可能的跳跃总步数
        for s in stones:
            for pre in dp[s]:
                for indent in [-1, 0, 1]:
                    step = pre + indent
                    if step > 0 and s + step in set_stones:
                        dp[s + step].add(step)


        return len(dp[stones[-1]]) > 0


# dfs + 二分 复杂度 n ^ 2 log(n)
import bisect
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        if stones[1] > 1: return False

        @lru_cache(None)
        def dfs(index, pre_step):
            if index == n - 1: return True

            for cur_step in range(pre_step - 1, pre_step + 2):
                if cur_step > 0:
                    next_index = bisect.bisect_left(stones, stones[index] + cur_step)
                    if index < next_index < n and stones[next_index] == stones[index] + cur_step:
                        if dfs(next_index, cur_step):
                            return True

            return False
        return dfs(1, 1)


print(Solution().canCross(stones=[0, 1, 3, 5, 6, 8, 12, 17]))

# dp[i][k] 表示青蛙能否达到「现在所处的石子编号」为 i 且「上一次跳跃距离」为 k的状态。

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        n = len(stones)
        dp = [[False] * n for i in range(n)]
        dp[0][0] = True

        for i in range(1, n):
            if stones[i] - stones[i - 1] > i:
                return False

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                k = stones[i] - stones[j]
                if k > j + 1:
                    break

                dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
                if i == n - 1 and dp[i][k]:
                    return True

        return False