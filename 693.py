class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        str1 = str(bin(n)[2:])
        flag = str1[0]
        for i in range(1, len(str1)):
            if str1[i] == flag:
                return False
            flag = str1[i]
        return True
