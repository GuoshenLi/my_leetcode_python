class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 2 == 0:
            n = n // 2
        return n == 1


# 位运算 如果是2的幂，必须要大于0并且 n & (n - 1) == 0 可以举例说明
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


