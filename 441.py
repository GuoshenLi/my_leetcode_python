class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1

        i = 1
        res = 0
        while n - i >= 0:

            n = n - i
            i += 1
            res += 1

        return res

# 二分查找也可以 自己找几个测试用例试试就行
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            sum = (1 + mid) * mid // 2

            if sum == n:
                return mid

            elif sum < n:
                left = mid + 1

            else:
                right = mid - 1

        return right