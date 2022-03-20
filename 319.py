from math import sqrt
# 模拟 超时
class Solution:
    def bulbSwitch(self, n: int) -> int:

        bulb_list = [False] * n
        for i in range(1, n + 1):
            index = i - 1
            while index < n:
                bulb_list[index] = not bulb_list[index]
                index += i

        return sum(bulb_list)


print(Solution().bulbSwitch(n = 1))


# 求1-n有多少个完全平方数
# 第1个灯泡 会在第1轮操作
# 第2个灯泡 会在第1,2轮操作
# 第3个灯泡 会在第1,3轮操作
# 第4个灯泡 会在第1,2,4轮操作
# 第5个灯泡 会在第1,5轮操作
# 第6个灯泡 会在第1,2,3轮操作
# 第7个灯泡 会在第1,7轮操作

# 很明显 若对于某一位置，操作轮数为奇数，则最终亮灯，若为偶数，则最终保持不亮。
# 因此求某一位置有多少个因数即可，若为奇数则亮，否则不亮。
# 而因数为奇数的正整数等价于完全平方数
# 所以1-n有多少个完全平方数即可

class Solution:
    def bulbSwitch(self, n: int) -> int:


        return int(sqrt(n))

# 算有多少个完全平方数

class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        res = 1
        count = 0
        while res * res <= n:
            res += 1
            count += 1

        return count