class Solution:
    def fractionAddition(self, expression: str) -> str:
        #1.将负号前面加一个+号
        #1.将负号前面加一个+号
        expression = expression.replace('-', '+-')
        if expression[0] == '+': expression = expression[1:]
        expression = expression.split('+')

        #2.依次相加
        ans_numerator, ans_denominator = 0, 1
        for fra in expression:

            new_numerator, new_denominator = fra.split('/')
            new_numerator, new_denominator = int(new_numerator), int(new_denominator)

            ans_numerator = ans_numerator * new_denominator + new_numerator * ans_denominator
            ans_denominator = ans_denominator * new_denominator

            gcd = self.greatest_common_devisor(abs(ans_numerator), abs(ans_denominator))
            ans_numerator = ans_numerator // gcd
            ans_denominator = ans_denominator // gcd

        return str(ans_numerator) + '/' + str(ans_denominator)



    # 最重要记住这个怎么求最大公约数 和 最小公倍数
    # 与正负无关，因此可以直接扔进去abs(a), abs(b) 死记硬背
    def greatest_common_devisor(self, a, b): # 用辗转相除法
        while b != 0:
            a, b = b, a % b
        return a

    def least_common_multiple(self, a, b): # 用 a * b - 最大公约数
        return a * b - self.greatest_common_devisor(a, b)



print(Solution().fractionAddition(expression="1/3-1/2"))