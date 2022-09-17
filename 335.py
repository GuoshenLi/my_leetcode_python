class Solution:
    def isSelfCrossing(self, x) -> bool:

        for i in range(3, len(x)):
            # 四条边相交的情况
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True

            # 五条边相交的情况
            if i >= 4 and x[i-1] == x[i-3] and x[i-4] + x[i] >= x[i-2]:
                return True

            # 六条边相交的情况
            if i >= 5 and x[i - 1] + x[i - 5] >= x[i - 3] and x[i - 2] <= x[i - 4] + x[i] and x[i - 4] <= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True
        return False