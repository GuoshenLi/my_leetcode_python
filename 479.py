class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1: return 9 # 只能是1 * 9　
        # 因为 9 * 9 最大是81 对应的回文串
        # 11, 22, 33, 44, 55, 66, 77 全部都不可能由两个一位数
        # 相乘得到

        # 两个最大的n数相乘 肯定是2n位数 偶数位 因此 9801 的回文 9889
        #
        # 所以说前半 half 就等于 max_num / (10 ** n)

        # 若n == 2: upper_bound = 99
        # n位数相乘的上限和下限
        upper_bound = (10 ** n) - 1
        lower_bound = upper_bound // 10 + 1

        max_num = upper_bound * upper_bound
        half = max_num // (10 ** n)

        isPalindrom = False
        while not isPalindrom:

            palindrom = self.creat_palindrom(half)
            for i in range(upper_bound, lower_bound - 1, -1):
                if i * i < palindrom:
                    break

                elif palindrom % i == 0:
                    # 如果能够执行到这一步说明
                    # palindrom // i的值一定 <= i. 这点非常重要
                    isPalindrom = True
                    break

            half -= 1

        return palindrom % 1337


    def creat_palindrom(self, num):
        return int(str(num) + str(num)[::-1])


