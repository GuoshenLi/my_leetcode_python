class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            return self.validate_IPv4(IP)
        elif IP.count(':') == 7:
            return self.validate_IPv6(IP)
        else:
            return "Neither"

    def validate_IPv4(self, IP):
        num_list = IP.split('.')
        for num in num_list:
            # 先考虑每部分的长度
            if len(num) == 0 or len(num) > 3:
                return 'Neither'

            # 不能有前导0 但是可以就一个0
            if len(num) > 1 and num[0] == '0':
                return 'Neither'

            # 是否有字母
            if not num.isdigit():
                return 'Neither'

            # 纯数字看是否大于255
            if int(num) > 255:
                return 'Neither'

        return 'IPv4'

    def validate_IPv6(self, IP):
        str_list = '0123456789abcdefABCDEF'
        num_list = IP.split(':')
        for num in num_list:
            # 若长度为0或大于4 不行
            if len(num) == 0 or len(num) > 4:
                return 'Neither'
            # 看看每个字母是不是都在str_list十六进制当中
            if not all(char in str_list for char in num):
                return 'Neither'

        return 'IPv6'