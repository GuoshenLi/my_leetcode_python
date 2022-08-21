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

# 时间复杂度更加低
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        diff_array = [0] * 26
        res = []
        length_s = len(s)
        length_p = len(p)

        if length_p > length_s: return []
        for i in range(length_p):
            diff_array[ord(s[i]) - ord('a')] += 1
            diff_array[ord(p[i]) - ord('a')] -= 1

        diff_count = [item != 0 for item in diff_array].count(True)
        if diff_count == 0:
            res.append(0)

        # diff_array 维护的是s比p差多少个
        for i in range(length_p, length_s):
            if diff_array[ord(s[i]) - ord("a")] == 0:  # 从相同变不同
                diff_count += 1
            elif diff_array[ord(s[i]) - ord("a")] == -1: # 从不同变相同
                diff_count -= 1

            diff_array[ord(s[i]) - ord("a")] += 1

            if diff_array[ord(s[i - length_p]) - ord("a")] == 1: # 从不同变相同
                diff_count -= 1
            elif diff_array[ord(s[i - length_p]) - ord("a")] == 0: # 从相同变不同
                diff_count += 1

            diff_array[ord(s[i - length_p]) - ord("a")] -= 1

            if diff_count == 0:
                res.append(i - length_p + 1)

        return res