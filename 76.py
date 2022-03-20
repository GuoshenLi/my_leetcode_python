from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        left = right = valid = 0
        res = ''
        length = float('inf')

        need = Counter(t)
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    length = right - left
                    res = s[left: right]

                d = s[left]
                left += 1

                if d in need:
                    # 只有相等才要 -1
                    if window[d] == need[d]:
                        valid -= 1

                    window[d] -= 1

        return res

