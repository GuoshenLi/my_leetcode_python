# 当前时刻攻击获得多少中毒时间要看后面的再次攻击的时间


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 0:
            return 0

        total = 0
        for i in range(1, n):
            total += min(timeSeries[i] - timeSeries[i - 1], duration)
        return total + duration

