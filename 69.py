# 牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        n, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + n / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(xi)


# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = x

        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

