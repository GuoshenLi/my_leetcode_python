class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            tmp = result[-1]

            if tmp[1] >= cur[0]:
                # 其实已经不用min了，所以可以不用min
                result[-1] = [min(cur[0], tmp[0]), max(cur[1], tmp[1])]
            else:
                result.append(cur)

        return result

# 2022.3.7
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1: return intervals
        intervals.sort(key = lambda x: x[0])

        # [[1, 3], [2, 6], [8, 10], [15, 18]]
        #                   i
        # res = [[1, 6]]
        # if intervals[i][0] <= res[-1][1]:
        #    合并
        #    res[-1][1] = max(res[-1][1], intervals[i][1])

        # if intervals[i][0] > res[-1][1]:
        #    新建 区间
        #    res.append(intervals[i])

        res = [intervals[0]]


        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res




