# 贪心算法 先对元素按第一个字母排序 然后指针指向每个区间的第二个位置 如果有重叠的话 指向最小的那个
# 只需要知道要弹出多少个而已

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])
        res = 0
        compare = intervals[0][1]

        for i in range(1, len(intervals)):

            if compare > intervals[i][0]:
                res += 1
                compare = min(compare, intervals[i][1])
            else:
                compare = intervals[i][1]

        return res