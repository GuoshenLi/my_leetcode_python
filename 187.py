class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        unique = {}
        res = []
        if len(s) < 10:
            return []

        for i in range(len(s)):
            slice = s[i: i + 10]
            if len(slice) == 10:
                unique[slice] = unique.get(slice, 0) + 1

        for k, v in unique.items():
            if v > 1:
                res.append(k)
        return res



# O（n）
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []
        get_binary = {"A": 0, "C": 1, "G": 2, "T": 3}
        window = 0
        table = defaultdict(int)
        res = []
        for i in range(10):
            window = (window << 2) | get_binary[s[i]]

        table[window] += 1

        for i in range(10, len(s)):
            window = ((window << 2) | get_binary[s[i]]) & ((1 << 20) - 1)

            table[window] += 1
            if table[window] == 2:
                res.append(s[i - 10 + 1: i + 1])

        return res

