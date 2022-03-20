# 超时
class Solution:
    def countDigitOne(self, n: int) -> int:

        count = 0
        for i in range(n + 1):
            count += str(i).count('1')

        return count






class Solution:
    def countDigitOne(self, n: int) -> int:
        high = n
        low = 0
        cur = 0
        count = 0
        base = 1

        while high != 0 or cur != 0:
            cur = high % 10
            high = high // 10
            # base 同样也说明low可以换多少个（在left可以选0 ~ left - 1的时候）
            if cur == 0: count += high * base
            elif cur == 1: count += high * base + 1 + low
            else: count += (high + 1) * base

            low = cur * base + low
            base *= 10

        return count

