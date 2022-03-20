# 一个套路的加法题
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i, j = len(a) - 1, len(b) - 1
        res = []
        carry = 0
        while i >= 0 and j >= 0:
            digit = (int(a[i]) + int(b[j]) + carry) % 2
            carry = (int(a[i]) + int(b[j]) + carry) // 2
            res.append(str(digit))
            i -= 1
            j -= 1

        while i >= 0:
            digit = (int(a[i]) + carry) % 2
            carry = (int(a[i]) + carry) // 2
            res.append(str(digit))
            i -= 1

        while j >= 0:
            digit = (int(b[j]) + carry) % 2
            carry = (int(b[j]) + carry) // 2
            res.append(str(digit))
            j -= 1

        if carry > 0:
            res.append('1')
        return ''.join(res[::-1])

