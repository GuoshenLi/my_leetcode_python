class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        result = 0
        index = len(g) - 1
        for i in range(len(s) - 1, -1, -1):
            while index >= 0 and g[index] > s[i]:
                index -= 1
            if index < 0:
                break
            result += 1
            index -= 1

        return result




class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        result = 0
        index = len(s) - 1
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                result += 1
                index -= 1

        return result
