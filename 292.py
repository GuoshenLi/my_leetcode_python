class Solution:
    def canWinNim(self, n: int) -> bool:
        # 找规律
        return (n % 4) != 0



class Solution:
    def canWinNim(self, n: int) -> bool:

        memo = [None for _ in range(n + 1)]
        # 1, 2,... , n    0不算
        def dfs(n):

            if n <= 3:
                return True
            elif memo[n] != None:
                return memo[n]


            if not dfs(n - 1) or not dfs(n - 2) or not dfs(n - 3):
                memo[n] = True
                return True
            else:
                memo[n] = False
                return False

        return dfs(n)

