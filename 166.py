# python 不会发生整数溢出
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negativeFlag = (numerator * denominator) < 0
        numerator = abs(numerator)
        denominator = abs(denominator)

        numlist = []
        pos = 0
        loop_Dict = {}
        loop_str = None

        while True:
            numlist.append(str(numerator // denominator))
            pos += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
                # 要么是整数，要么是有限小数

            if numerator not in loop_Dict:
                loop_Dict[numerator] = pos

            else:
                # 开始循环了，因此截断
                first_loc = loop_Dict[numerator]
                loop_str = ''.join(numlist[first_loc: pos])
                break

        ans = numlist[0]
        if len(numlist) > 1:
            ans += '.'

        if loop_str:
            # 1 / 6

            ans += ''.join(numlist[1:first_loc]) + '(' + ''.join(loop_str) + ')'
        else:
            ans += ''.join(numlist[1:])

        if negativeFlag == True:
            ans = '-' + ans
        return ans