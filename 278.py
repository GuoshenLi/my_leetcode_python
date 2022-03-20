# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
# 线性查找 超时
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """


        for i in range(1, n + 1):
            if isBadVersion(i):
                return i


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
# 二分查找 简单
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

