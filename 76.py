from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        left, right, valid, needs = 0, 0, 0, Counter(t)
        window = defaultdict(int)
        min_len = float("+inf")
        res = ""
        while right < n:

            c = s[right]
            right += 1

            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1

            while valid == len(needs):
                if right - left < min_len:
                    min_len = right - left
                    res = s[left: right]

                d = s[left]
                left += 1

                if d in needs:
                    if needs[d] == window[d]:
                        valid -= 1

                    window[d] -= 1

        return res


from collections import defaultdict, Counter

class Solution:
    def is_contain(self, window, needs):
        for char in needs.keys():
            if window[char] < needs[char]:
                return False

        return True

    def minWindow(self, s: str, t: str) -> str:
        needs = Counter(t)
        window = defaultdict(int)
        '''
            s = "A D O B E C O D E B A N C", t = "ABC"
                 l
                   r

            window 只用存下来 t里面有的元素的个数即可
        '''
        res = ""
        left = 0
        right = 0
        valid = 0
        min_length = float("+inf")

        while right < len(s):
            c = s[right]
            right += 1

            window[c] += 1

            # 满足条件的时候 再退出来left
            while self.is_contain(window, needs):
                if right - left < min_length:
                    min_length = right - left
                    res = s[left: right]

                d = s[left]
                window[d] -= 1
                left += 1

        return res


print(Solution().minWindow(s =
"ADOBECODEBANC", t="ABC"
))