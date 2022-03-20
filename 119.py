class Solution:
    # 后一项 等于前一项前后加0 再对应元素相加
    def getRow(self, rowIndex: int) -> List[int]:

        res = [1]
        for i in range(1, rowIndex + 1):
            tmp = []
            res_1 = res[:]
            res_2 = res[:]
            res_1.insert(0, 0)
            res_2.append(0)
            for j in range(i + 1):
                tmp.append(res_1[j] + res_2[j])
            res = tmp[:]

        return res

# 不用引用，更加简化的版本
class Solution:
    # 后一项 等于前一项一开始插入0 再对应元素相加
    def getRow(self, rowIndex: int) -> List[int]:

        res = [1]
        for i in range(1, rowIndex + 1):
            res.insert(0, 0)
            for j in range(i):
                res[j] = res[j] + res[j + 1]

        return res
