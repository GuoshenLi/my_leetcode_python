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



# 用这种方法就可以了
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # 如果某一位不可以被3整除的话，那个就证明只出现一次的数字在这一位为1
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1

            # res |= (count % 3) << i
            if count % 3 != 0:
                res |= 1 << i

        # 对最高位进行判断
        # 因为最高位（第32位）是负号位

        return res - 2 ** 32 if res >> 31 & 1 else res
        # 的确要减掉2 ** 32, 因为原来按照正数算 因此要换成负数所以差2 ** 32





# 考逻辑电路 只能背 有限状态机 忽略

# 代码参考热评。解释下：假设有一个数为x,那么则有如下规律：
# 0 ^ x = x,
# x ^ x = 0；
# x & ~x = 0,
# x & ~0 =x;

# -那么就是很好解释上面的代码了。一开始a = 0, b = 0;
# x第一次出现后，a = (a ^ x) & ~b的结果为 a = x, b = (b ^ x) & ~a的结果为此时因为a = x了，所以b = 0。
# x第二次出现：a = (a ^ x) & ~b, a = (x ^ x) & ~0, a = 0; b = (b ^ x) & ~a 化简， b = (0 ^ x) & ~0 ,b = x;
# x第三次出现：a = (a ^ x) & ~b， a = (0 ^ x) & ~x ,a = 0; b = (b ^ x) & ~a 化简， b = (x ^ x) & ~0 , b = 0;所以出现三次同一个数，a和b最终都变回了0.

# 只出现一次的数，按照上面x第一次出现的规律可知a = x, b = 0;因此最后返回a.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0

        for num in nums:
            a = (a ^ num) & ~b
            b = (b ^ num) & ~a
        return a
