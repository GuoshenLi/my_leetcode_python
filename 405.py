class Solution:
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF
        # python求一个数的补码一定要这样做！
        # 那么正数的补码为其原码，负数的补码则为其取反再加1
        # 死背python如何求补码
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111
        while num > 0:
            res += s[num & mask]
            num >>= 4
        return res[::-1] if res else "0"

