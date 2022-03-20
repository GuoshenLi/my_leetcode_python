class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        k = 1
        length_a = len(a)
        length_b = len(b)
        res = length_a

        # 加到res的长度大于等于length_b

        while res < length_b:
            k += 1
            res += length_a

        if b in k * a:
            return k

        if b in (k + 1) * a:
            return k + 1

        return -1
