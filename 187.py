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
