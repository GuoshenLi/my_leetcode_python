class Solution:
    def addDigits(self, num: int) -> int:

        while num // 10 != 0:
            res = 0
            while num > 0:
                res += num % 10
                num = num // 10

            num = res

        return num

# O(1) 复杂度 最优解
# 自己在纸上写出来找规律 很明显答案在1-9循环
class Solution:
    def addDigits(self, num: int) -> int:
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
        return num
