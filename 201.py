# 找公共前缀
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift



# 最 naive 但是 超时
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = m
        while m <= n:
            count = count & m
            m += 1
        return count