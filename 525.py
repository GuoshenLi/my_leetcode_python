from typing import List
# 暴力 严重超时
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i : j + 1].count(0) == nums[i : j + 1].count(1):
                    res = max(res, j - i + 1)

        return res


# 连续子数组 都用哈希表加前缀和 同样 O(n^2)不能通过

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        res = 0
        for i in range(len(pre_sum)):
            for j in range(i + 2, len(pre_sum)):
                if pre_sum[i] == pre_sum[j]:
                    res = max(res, j - i)


        return res



# 和523 一样 前缀和加哈希表 一定要{0:-1}
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_sum = 0
        hash_map = {0 : -1}
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pre_sum -= 1
            else:
                pre_sum += 1

            if hash_map.get(pre_sum) is not None:
                res = max(res, i - hash_map[pre_sum])
            else:
                # 因为要最长子数组 因此 pre_sum 没有出现过再写入哈希表
                # 如果已经出现过的话不用更新 因为我们要前面的那个才能有更长的结果
                hash_map[pre_sum] = i

        return res


print(Solution().findMaxLength(nums=[0,1,0]))