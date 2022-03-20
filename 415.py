class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = len(num1) - 1
        j = len(num2) - 1
        res = []
        carry = 0
        while i >= 0 and j >= 0:
            res.append((int(num1[i]) + int(num2[j]) + carry) % 10)
            carry = (int(num1[i]) + int(num2[j]) + carry) // 10
            i -= 1
            j -= 1

        while i >= 0:
            res.append((int(num1[i]) + carry) % 10)
            carry = (int(num1[i]) + carry) // 10
            i -= 1

        while j >= 0:
            res.append((int(num2[j]) + carry) % 10)
            carry = (int(num2[j]) + carry) // 10
            j -= 1

        if carry > 0:
            res.append(1)


        return ''.join(map(str, res[::-1]))