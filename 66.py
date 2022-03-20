# 与链表相加类似
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digit = (digits[-1] + 1) % 10
        carry = (digits[-1] + 1) // 10
        digits[-1] = digit

        for i in range(len(digits) - 2, -1, -1):
            digit = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = digit

        if carry == 1:
            digits = [1] + digits

        return digits




# 粗暴 直接转换为数字
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        res = []
        for i in range(len(digits)):
            num = num * 10 + digits[i]

        num += 1

        for i in str(num):
            res.append(int(i))


        return res