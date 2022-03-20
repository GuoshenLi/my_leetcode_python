# 转换成分钟 排序
from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        length = len(timePoints)
        if len(timePoints) > len(set(timePoints)):
            return 0

        for i in range(length):
            hour = int(timePoints[i].split(':')[0])
            minute = int(timePoints[i].split(':')[1])
            timePoints[i] = hour * 60 + minute

        timePoints.sort()
        res = float("inf")
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i - 1])

        # 因为钟是圆的 然后注意算 第一个与最后一个的时间差
        return min(res, timePoints[0] + 1440 - timePoints[-1])



print(Solution().findMinDifference(timePoints = ["23:59","00:00"]))