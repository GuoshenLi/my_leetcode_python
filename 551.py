from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'LLL' not in s


class Solution:
    def checkRecord(self, s: str) -> bool:

        #判断是否存在超过两个连续的'L'
        def pending_s(s):
            count = 0
            res = 0
            for i in range(len(s)):
                if s[i] == "L":
                    count += 1
                else:
                    res = max(res, count)
                    count = 0
            return max(res, count)


        #不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到)
        return s.count("A") <= 1 and pending_s(s) <= 2



# Solution().checkRecord(s = 'LALL')


# 记住判断特定连续字符的最长个数
def pending_s(s):
    count = 0
    res = 0
    for i in range(len(s)):
        if s[i] == "p":
            count += 1
        else:
            res = max(res, count)
            count = 0
    return max(res, count)


print(pending_s(s = 'ppppasdasdasdppappppppp'))