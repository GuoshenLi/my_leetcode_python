class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = set()


    def addNum(self, val: int) -> None:
        if val not in self.l:
            self.l.add(val)

    def getIntervals(self) -> List[List[int]]:
        # 典型的双指针
        l = list(self.l)
        l.sort()
        res = []
        if len(l) == 1:
            res.append([l[0], l[0]])
            return res

        left, right = 0, 1

        while right < len(l):
            if l[right] == l[right - 1] + 1:
                right += 1

            else:
                res.append([l[left], l[right - 1]])
                left = right
                right += 1
        # 最后那里 要再加一个判断 常规操作
        res.append([l[left], l[right - 1]])
        return res



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()