# 快速幂求模
# 双重递归

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = self.mypow(a, last)
        part2 = self.mypow(self.superPow(a, b), 10)
        return part1 * part2 % 1337

    def mypow(self, a, k, base=1337):
        if k == 0:
            return 1
        y = self.mypow(a, k // 2)
        if k % 2 == 1:
            return (a * y * y) % base
        if k % 2 == 0:
            return (y * y) % base



# 只有这样写快速幂才不会超时！！！
from typing import List
class Solution:
    def superPow(self, a: int, b: int) -> int:
        if b == 0:
            return 1
        y = self.superPow(a, b // 2)
        if b % 2 != 0:
            return y * y * a

        else:
            return y * y


