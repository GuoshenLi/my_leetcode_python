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

