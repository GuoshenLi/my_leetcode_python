# 回溯

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(index, tmp):
            if len(tmp) == k:
                res.append(tmp[:])

            for j in range(index, n):
                tmp.append(j + 1)
                dfs(j + 1, tmp)
                tmp.pop()

        dfs(0, [])

        return res
