class Solution:
    def findComplement(self, num: int) -> int:

        return int(bin(num)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)
        # int 是以base为2去算十进制数 会自动去掉前导0




class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]

        res = ''

        for char in binary:
            if char == '0':
                res += '1'
            else:
                res += '0'

        return int(res, 2)




class Solution:
    def findComplement(self, num: int) -> int:

    # 5的二进制是：0101，7的二进制是： 0111，它们的抑或为：0010，去掉前导零位即为取反。
    # 再来一个例子，假设a为1110 0101，b为1111 1111，a^b = 0001 1010是a的取反。也就是说二进制位数与num相同，且全为1的数tmp
    # 与num的抑或即为所求。

        tmp = 1
        while tmp < num:
            tmp = tmp << 1
            tmp = tmp + 1
        return tmp ^ num
