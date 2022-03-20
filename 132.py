class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[True] * n for _ in range(n)]
        # 注意回文串打表 都是这种打表顺序

        # 判断一个字符串两两任意位置是否回文
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                g[i][j] = (s[i] == s[j]) and g[i + 1][j - 1]

        # f[i] 表示[0, i]变成回文子串最少要切多少刀。

        f = [float("inf")] * n

        for i in range(n):
            if g[0][i]:
                f[i] = 0

        for i in range(n):
            for j in range(i):
                if g[j + 1][i]:
                    f[i] = min(f[i], f[j] + 1)

        return f[n - 1]

