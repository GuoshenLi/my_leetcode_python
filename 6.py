class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ['' for i in range(numRows)]
        flag = True
        index = 0

        for i in range(len(s)):
            res[index] += s[i]

            if index == 0:
                flag = True

            elif index == numRows - 1:
                flag = False


            if flag == True:
                index += 1

            elif flag == False:
                index -= 1


        return ''.join(res)
