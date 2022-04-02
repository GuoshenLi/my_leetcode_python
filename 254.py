from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        if n == 1: return []
        res = []
        factors = [i for i in range(2, n - 1) if n % i == 0]
        length = len(factors)

        def dfs(index, product, tmp):
            if product == n:
                res.append(tmp[:])
                return None

            for i in range(index, length):
                # i == 2 -> n - 1
                if product * factors[i] <= n:
                    tmp.append(factors[i])
                    dfs(i, product * factors[i], tmp)
                    tmp.pop()

        dfs(0, 1, [])
        return res

