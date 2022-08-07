class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:

        i, j, sum_ = 1, 1, 0
        res = []

        while j < target:

            if sum_ < target:
                sum_ += j
                j += 1
            elif sum_ > target:
                sum_ -= i
                i += 1
            else:
                res.append(list(range(i, j)))
                sum_ -= i
                i += 1
                # 也可以这样：
                # sum_ += j
                # j += 1
        return res