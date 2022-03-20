# 也可以append进来然后套用56的代码
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        while i <= n - 1 and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i <= n - 1 and intervals[i][0] <= newInterval[1]:
            # 这个判断很关键        判断条件是这个的原因是因为要和下面互异
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i <= n - 1 and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        return res










