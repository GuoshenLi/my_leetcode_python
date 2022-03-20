# 暴力解法 超时
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        sum = 0
        i = 1
        while i < num:

            if num % i == 0:
                sum += i

            i += 1

        return sum == num



class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        sum = 1

        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum += i
                sum += num // i

        return sum == num


