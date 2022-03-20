# 十进制转二十六进制
class Solution:
    def convertToTitle(self, n: int) -> str:

        table = {
        26: 'Z', 25: 'Y',
        24: 'X', 23: 'W', 22: 'V', 21: 'U',
        20: 'T', 19: 'S', 18: 'R', 17: 'Q',
        16: 'P', 15: 'O', 14: 'N', 13: 'M',
        12: 'L', 11: 'K', 10: 'J', 9: 'I',
        8: 'H', 7: 'G', 6: 'F', 5: 'E',
        4: 'D', 3: 'C', 2: 'B', 1: 'A'
        }


        s = ''
        while(n):
            n -= 1
            s = table[n % 26 + 1] + s
            n = n // 26
        return s

class Solution:
    def convertToTitle(self, n: int) -> str:

        s = ''
        while(n):
            n -= 1
            s = chr(n % 26 + ord('A')) + s
            n = n // 26

        return s

