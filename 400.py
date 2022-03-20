# 暴力解法 超时
class Solution:
    def findNthDigit(self, n: int) -> int:

        count = 0
        i = 0
        while True:
            i += 1
            for index in range(len(str(i))):
                count += 1
                if count == n:
                    return int(str(i)[index])


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 找到对应的属于第几组数字
        base = 9
        count = 1
        while n - base * count > 0:
            n -= base * count
            base *= 10
            count += 1

        # base = 90
        # count = 2
        # 第141个数字
        number = 1

        for i in range(1, count):
            number *= 10
        # 找到第二组的哪一个数字的哪一位
        # 如果time == 1，则说明答案为这个数字number往右移动一位的个位
        # 如果time == 2，则说明答案为这个数字number往右移动二位的个位
        # 若整除，则直接选个位

        # 141 // 2
        mod = n % count
        if mod == 0:
            time = count
            number += n // count - 1
        else:
            number += n // count
            time = mod

        for i in range(time, count):
            number = number // 10
        return number % 10


print(Solution().findNthDigit(n = 141))