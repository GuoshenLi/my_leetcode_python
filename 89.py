# 牛逼 镜面反射法
from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        multiple = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] + multiple)
            multiple = multiple * 2

        return res



# 死背结论 第k个格雷码： G(k) = k ^ (k // 2)
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(2 ** n):
            res.append(i ^ (i >> 1))
        return res





print(Solution().grayCode(n = 3))