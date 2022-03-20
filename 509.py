class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)



# 加一个memo数组
class Solution:
    def fib(self, n: int) -> int:
        memo = [None] * (n + 1)

        def dfs(n):
            if n == 0:
                return 0

            if n == 1:
                return 1

            if memo[n]:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)

            return memo[n]

        return dfs(n)

