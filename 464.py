from typing import List
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal : return False
        # 判断两种极端情况
        # 1,2,...,maxChoosableInteger 加起来都比desiredtotal要小 谁都赢不了

        memo = [None] * (1 << maxChoosableInteger)
        # 为什么要移动maxChoosableInteger?
        # 假设maxChoosableInteger 是 3
        # 1,1,1 所以说最大应该是这个
        # 因此要移动3位 才可以完全包括它
        # 1,0,0,0 比最大的数字大1
        def dfs(state, cum_sum):
            if memo[state] != None:
                return memo[state]
            for choose in range(1, maxChoosableInteger + 1):
                cur = 1 << (choose - 1)
                if cur & state != 0: # 已经选过这个动作
                    continue

                if choose + cum_sum >= desiredTotal or not dfs(state | cur, choose + cum_sum):
                    # 博弈论这个一定要加not 对方要输
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dfs(0, 0)


# 超时
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal : return False

        # 判断两种极端情况
        # 1,2,...,maxChoosableInteger 加起来都比desiredtotal要小 谁都赢不了

        visited = [0] * (maxChoosableInteger + 1)
        memo = {}

        def dfs(visited, cum_sum):
            state = str('-'.join(map(str, visited)))
            if state in memo:
                return memo[state]
            if cum_sum >= desiredTotal: return False

            for i in range(1, maxChoosableInteger + 1):
                if visited[i] == 1: continue
                visited[i] = True
                last = dfs(visited, cum_sum + i)
                visited[i] = False
                if not last:

                    memo[sta] = True
                    return True
            memo[state] = False
            return False


        return dfs(visited, 0)


        return dfs(visited, 0)

print(Solution().canIWin(maxChoosableInteger = 10, desiredTotal = 40))