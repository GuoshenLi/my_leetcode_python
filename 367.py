class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        n = 1
        while True:
            if n ** 2 < num:
                n = n + 1
            elif n ** 2 == num:
                return True
            else:
                return False

# 二分查找
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 1, num

        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1

        return False

