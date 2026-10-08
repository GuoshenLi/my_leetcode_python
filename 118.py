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


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        '''
            [1, 2, 1]
        '''

        res = [[1]]

        for i in range(1, numRows):
            this_level = res[-1][:]
            this_level.insert(0, 0)

            for j in range(i):
                this_level[j] = this_level[j] + this_level[j + 1]
            res.append(this_level)

        return res