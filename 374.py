# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
# 二分查找
class Solution:
    def guessNumber(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1

