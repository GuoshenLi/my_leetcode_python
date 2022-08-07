'''
约瑟夫环 背公式
'''
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:

        if n == 0: return 0

        return (self.lastRemaining(n - 1, m) + m) % n




class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x

