# 前缀和 超时
# 72 / 89 个通过测试用例
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre_sum = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        res = 0

        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                # 其实就是sum中 [i, j - 1]的和
                if pre_sum[j] - pre_sum[i] == k:
                    res += 1

        return res


# 就背诵这一版代码 容易理解
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        # 目的都是要枚举[i, j) i < j

        table = {0: 1} #

        res = 0
        for j in range(1, n + 1):
            # 为什么从1 开始 因为j要领先 i 而i==0 因此j只能从1开始

            # pre_sum[j] - pre_sum[i] == k
            # pre_sum[i] = pre_sum[j] - k

            if pre_sum[j] - k in table:
                res += table[pre_sum[j] - k]

            table[pre_sum[j]] = table.get(pre_sum[j], 0) + 1

        return res



# 模版
# 前缀和 哈希表 记住要用哈希表的话不用数组存前缀和
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # hasp_map存的是前缀和的个数
        hash_map = {0: 1}  # 一定要有这个 要么就{0: -1}其他两个题目
        # 如果前缀和就是从一开始累加到给订位置 则启动{0: 1}
        # [1,1,1] k = 2, 那么在下标为1的时候就会启动{0: 1}

        res = 0
        pre = 0

        for i in range(len(nums)):
            pre += nums[i]
            # pre - k 要么得到的就是i这个位置本身，要么就是要么就是从前              # 面到i这个位置的和 (压根不用担心有没有越界有没有重复)

            if pre - k in hash_map:
                res += hash_map[pre - k]

            hash_map[pre] = hash_map.get(pre, 0) + 1

        return res



print(Solution().subarraySum(nums = [1,1,1], k = 2))