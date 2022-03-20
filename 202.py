class Solution:
    def isHappy(self, n: int) -> bool:

        loop = {n}

        while n != 1:
            tmp = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                tmp += digit ** 2

            n = tmp
            if n in loop:
                return False
            loop.add(n)

        return True


