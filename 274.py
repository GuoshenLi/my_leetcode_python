# 与275一样 要先排序
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for h in range(len(citations), 0, -1):
            if citations[n - h] >= h:
                return h

        return 0


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 有h篇论文的引用大于等于h 的最大的h
        # 可以知道h的范围0 ~ len(citations)

        n = len(citations)
        citations.sort()


        for i in range(n):
            # 有n - i篇论文的引用次数 >= citations[i] 天然成立
            # 根据定义 如果有h篇论文的引用 >= h的话 h就为所求 (最大的)
            # 那么因此 citations[i] >= n - i (利用了传递性) 那么n - i即为所求 传递性 牛逼!
            # 并且肯定是最大的 因为i从小开始遍历 n - i 从大开始 因此肯定最大

            if citations[i] >= n - i:
                return n - i

        return 0


