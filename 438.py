from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        length_p = len(p)
        count_p = Counter(p)
        res = []
        for start in range(len(s) - length_p + 1):
            if count_p == Counter(s[start:start + length_p]):
                res.append(start)


        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_array = [0] * 26
        window_array = [0] * 26
        length_p = len(p)
        length_s = len(s)
        if length_s < length_p:
            return []
        res = []
        for i in range(length_p):
            p_array[ord(p[i]) - ord('a')] += 1
            window_array[ord(s[i]) - ord('a')] += 1
        if p_array == window_array:
            res.append(0)

        for i in range(length_p, length_s):
            window_array[ord(s[i - length_p]) - ord('a')] -= 1
            window_array[ord(s[i]) - ord('a')] += 1
            if p_array == window_array:
                res.append(i - length_p + 1)

        return res