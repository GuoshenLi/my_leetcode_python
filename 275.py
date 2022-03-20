class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # 线性扫描
        # 只用关注 有h篇论文的引用大于等于h
        # 求这个对答h
        # 因此h的范围是 0 ~ len(citations)

        # 因为要求最大的 所以就要从大的开始遍历

        n = len(citations)
        for h in range(n, 0, -1):
            if citations[n - h] >= h:
                return h
        return 0




# 二分 citations[mid] >= n - mid 要找满足条件的最小的mid
# 可以套用模版

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        if citations[-1] == 0: return 0
        while l < r:
            mid = (l + r) // 2
            if citations[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1

        return n - l