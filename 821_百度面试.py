# 百度面试
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        index = []
        res = []
        for i in range(len(S)):
            if S[i] == C:
                index.append(i)

        for i in range(len(S)):
            res.append(min(abs(i - ind) for ind in index))

        return res