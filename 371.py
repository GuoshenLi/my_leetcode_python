class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        MASK = 2 ** 32

        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK

        return a - 2 ** 32 if a >> 31 & 1 else a

# 死背 和 gcd差不多



class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        def helper(a, b):
            # 这种处理很常见
            if b == 0: return a - 2 ** 32 if a >> 31 == 1 else a
            MASK = 2 ** 32
            # 限制范围在[0, 2 ** 32 - 1]
            return helper((a ^ b) % MASK, ((a & b) << 1) % MASK)

        return helper(a, b)

