# 找规律
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for level in range(2, numRows):
            level_res = []
            level_res.append(1)
            for i in range(1, level):
                level_res.append(res[level - 1][i - 1] + res[level - 1][i])
            level_res.append(1)
            res.append(level_res)

        return res