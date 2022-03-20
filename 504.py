# 504 十进制转换成其他进制就是除那个数取余
# 短除法


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ans = []
        is_negative = num < 0
        num = abs(num)
        while num > 0:
            remain = num % 7
            num = num // 7
            ans.append(str(remain))

        return "-" + "".join(ans[::-1]) if is_negative else "".join(ans[::-1])


