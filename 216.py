class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        def dfs(start, tmp):
            if len(tmp) == k and sum(tmp) == n:
                res.append(tmp[:])
                return None

            for i in range(start, 10):
                tmp.append(i)
                dfs(i + 1, tmp)
                tmp.pop()

        dfs(1, [])
        return res



