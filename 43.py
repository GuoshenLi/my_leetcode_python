# 中等题目 我觉得是简单题
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        m = len(num1)
        n = len(num2)
        if num1 == "0" or num2 == "0": return "0"

        res = "0"
        for j in range(n - 1, -1, -1):
            temp = ['0'] * (n - j - 1)
            carry = 0

            for i in range(m - 1, -1, -1):
                digit = (carry + int(num2[j]) * int(num1[i])) % 10
                carry = (carry + int(num2[j]) * int(num1[i])) // 10
                temp.append(str(digit))

            if carry != 0:
                temp.append(str(carry))

            temp.reverse()
            res = self.add_two_string(res, temp)

        return res

    def add_two_string(self, num1, num2):

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




# 斯坦福Karatsuba算法
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1) < 10 or int(num2): return str(int(num1) * int(num2))

        m = len(num1)
        n = len(num2)

        a, b = int(num1) // (10 ** (m // 2)), int(num1) % (10 ** (m // 2))
        c, d = int(num2) // (10 ** (n // 2)), int(num2) % (10 ** (n // 2))

        ac = self.multiply(str(a), str(c))
        bd = self.multiply(str(b), str(d))

        ad = self.multiply(str(a), str(d))
        bc = self.multiply(str(b), str(c))

        return str((10 ** (m // 2 + n // 2)) * int(ac) + 10 ** (m // 2) * int(ad) + 10 ** (n // 2) * int(bc) + int(bd))



# O(log(num1)) 时间复杂度 的解法
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        num1 = int(num1)
        num2 = int(num2)
        res = 0
        while num1 > 0:
            if num1 % 2 == 0:
                num1 //= 2
                num2 += num2

            else:
                res += num2
                num1 -= 1


        return str(res)

