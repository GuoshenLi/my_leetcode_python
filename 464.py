# 超时
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal : return False

        # 判断两种极端情况
        # 1,2,...,maxChoosableInteger 加起来都比desiredtotal要小 谁都赢不了

        memo = {}
        def dfs(state, cur_sum):
            if cur_sum >= desiredTotal: return False
            if state in memo: return memo[state]
            for choose in range(1, maxChoosableInteger + 1):
                cur = 1 << (choose - 1)
                if cur & state != 0:
                    continue

                result = dfs(cur | state, cur_sum + choose)
                if not result:
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

                    memo[state] = True
                    return True
            memo[state] = False
            return False


        return dfs(visited, 0)


        return dfs(visited, 0)

print(Solution().canIWin(maxChoosableInteger = 10, desiredTotal = 40))