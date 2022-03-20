

# 暴力法完全超时
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        table = [[0 for _ in range(n)] for _ in range(m)]

        for x_, y_ in ops:
            for i in range(x_):
                for j in range(y_):
                    table[i][j] += 1

        res = 0

        for i in range(m):
            for j in range(n):
                if table[i][j] == table[0][0]:
                    res += 1

        return res



# 取一个交集即可

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])

        return m * n




