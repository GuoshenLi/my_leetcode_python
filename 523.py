from typing import List
# 枚举所有长度大于等于2的子串 记住方法
# 和枚举所有子序列不一样
# 超出时间限制

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        length = len(nums)

        for i in range(length):
            for j in range(i + 1, length):
                sum_ = 0
                start = i
                while start <= j:
                    sum_ += nums[start]
                    start += 1

                if sum_ == k or sum_ % k == 0:
                    return True

        return False

# 他妈的这个还会超时
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 前缀和

        n = len(nums)
        pre_sum = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        for i in range(n + 1):
            for j in range(i + 2, n + 1):
                if (pre_sum[j] - pre_sum[i]) % k == 0:
                    return True

        return False



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        Hash  = {0: -1}
        residual = 0
        for j in range(len(nums)):
            residual += nums[j]
            if k != 0:
                residual = residual % k
            if Hash.get(residual) is not None:
                if j - Hash[residual] >= 2:
                    return True
            else:
                Hash[residual] = j

            # 如果不存在才更新 这样子才可能获得更大的窗口
        return False


##### 就按这一版代码去做！！！
###
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2: return False
        if k == 0: return True

        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]

        table = {0: 0}
        # table其实是存储左边的前缀和
        # presum[j] - presum[i] [i, j)开区间
        # 存储的其实就是0对应的下标

        for j in range(1, n + 1):
            if pre_sum[j] % k in table:
                if j - table[pre_sum[j] % k] >= 2:
                    # 其实就是区间[table[pre_sum[j] % k], j)
                    #
                    return True
            else:
                # 因为我要更长的序列 所以pre_sum[j] % k不在table才要更新
                table[pre_sum[j] % k] = j

        return False




#
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         if len(nums) < 2:
#             return False
#         if k == 0:
#             return True
#
#         Hash = {0: -1} # 如果前缀和下标例如从0下标开始到3，就要通过和这个哈希表的{0:-1}与-1做减法
#         # (sum1 - sum2) % k == 0 也就是 sum1 % k = sum2 % k
#         # 有可能sum2本来就等于0 也就是sum1 自己就可以整除 这样子的话就要用到{0:-1}
#         # 例如[2,3,4,4,5] 若k == 3 那么[2,3,4]之和就可以整除3 因此sum1就为9 sum2没有 这样子下标就应该是2第三个数减 (-1)
#         # 得到长度为3才可以得到正确的长度为3
#         # index 为 -1
#         residual = 0
#         for j in range(len(nums)):
#             residual += nums[j]
#             if k != 0:
#                 residual = residual % k
#             if Hash.get(residual) is not None:
#                 if j - Hash[residual] >= 2:
#                     return True
#             else:
#                 Hash[residual] = j
#         return False
#
#
# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         if len(nums) < 2: return False
#         if k == 0: return True
#
#         table = {0: -1}
#         pre = 0
#
#         for i in range(len(nums)):
#             pre += nums[i]
#
#             if pre % k in table:
#                 if i - table[pre % k] >= 2:
#                     return True
#             else:
#                 # 因为我要更长的序列 所以pre % k不在table才要更新
#                 table[pre % k] = i
#
#         return False


print(Solution().checkSubarraySum(nums=[23,2,4,6,7], k = 7))