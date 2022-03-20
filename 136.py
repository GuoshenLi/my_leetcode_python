class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        appear = {}

        for num in nums:
            if num not in appear:
                appear[num] = 1
            else:
                appear[num] += 1

        for k, v in appear.items():
            if v == 1:
                return k
# 考位运算 只能背
class Solution:
    # 0 ^ a = a
    # a ^ a = 0
    # 另外 异或满足交换律 若nums = [1,2,3,3,2]
    # 0 ^ 1 ^ 2 ^ 3 ^ 3 ^ 2
    # 等于
    # 0 ^ 2 ^ 2 ^ 3 ^ 3 ^ 1
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num

        return res


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # 如果某一位不可以被3整除的话，那个就证明只出现一次的数字在这一位为1
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1

            res |= (count % 2) << i

        # 对最高位进行判断
        # 因为最高位（第32位）是负号位
        return res - 2 ** 32 if res >> 31 & 1 else res