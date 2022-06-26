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
