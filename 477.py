# 暴力 超时
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        res = 0

        def HammingDistance(num1, num2):
            tmp = 0
            for _ in range(32):
                if num1 & 1 != num2 & 1:
                    tmp += 1
                num1 = num1 >> 1
                num2 = num2 >> 1

            return tmp

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                res += HammingDistance(nums[i], nums[j])

        return res


    class Solution:

        # 4： 0 1 0 0
        # 14：1 1 1 0
        # 2： 0 0 1 0
        # -------------
        # 第高位：两个0，一个1， 有2*1个
        # 其次为：两个1，一个0， 有2*1个
        # 其次位：两个1，一个0， 有2*1个
        # 最低位：三个零，      有3*0个
        # 最后得6


        def totalHammingDistance(self, nums: List[int]) -> int:
            res, n = 0, len(nums)
            for i in range(32):
                cnt_1 = 0
                for j in range(n):
                    cnt_1 += (nums[j] >> i) & 1
                res += (n - cnt_1) * cnt_1
            return res

