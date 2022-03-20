class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0:
            return False
        while n % 4 == 0:
            n /= 4
        return n == 1


# 在2的幂次基础上做
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & 0xaaaaaaaa == 0



# 数学
from math import log2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log2(num) % 2 == 0

