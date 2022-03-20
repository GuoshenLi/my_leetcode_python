class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map_dict = {}

        i = 0
        while i < len(s):

            if s[i] in map_dict:
                target = map_dict[s[i]]
                if target != t[i]:
                    return False
            else:
                if t[i] in map_dict.values():
                    return False
                map_dict[s[i]] = t[i]
            i += 1

        return True


# 维护两张哈希表 记录顺过来和反过去的映射
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s2t = {}
        t2s = {}

        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i] or t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]

        return True

