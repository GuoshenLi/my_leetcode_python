class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        count_dict = {}

        for item in nums:
            count_dict[item] = count_dict.get(item, 0) + 1
        res = []
        for k, v in count_dict.items():
            if v == 1:
                res.append(k)

        return res

# 位运算 巧妙
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0

        for n in nums:
            xor ^= n
        # 得到的xor是两个单独数字的异或

        mask = 1
        while mask & xor == 0:
            mask <<= 1
        # 按照不同的那一位对整个数组进行分组
        # 左移mask，移动到xor为1的那一位，也是单独数字存在差异的一位
        num1, num2 = 0, 0

        for n in nums:
            # 按照差异，对数组分组，两个单独数字被分到不同的组
            if n & mask == 0:
                num1 ^= n
            else:
                num2 ^= n

        return [num1, num2]
