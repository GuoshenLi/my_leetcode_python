import math
# 对a进行遍历即可 看b能不能被开根号为整数
# 注意a == 0或b ==0都可以

class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        a = 0

        while c - a ** 2 >= 0:

            b = math.sqrt(c - a ** 2)
            if b == int(b):
                return True
            a += 1

        return False