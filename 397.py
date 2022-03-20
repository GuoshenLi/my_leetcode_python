# dfs
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n - 1), self.integerReplacement(n + 1)) + 1


# bfs
# 本质上就是暴力
class Solution:
    def integerReplacement(self, n: int) -> int:
        Q = collections.deque()
        Q.append([n, 0])
        while Q:
            v, k = Q.popleft()
            if v == 1:
                return k
            elif v % 2 == 0:
                Q.append([v // 2, k + 1])
            else:
                Q.append([v - 1, k + 1])
                Q.append([v + 1, k + 1])
