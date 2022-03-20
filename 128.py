# 最简单的暴力法
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        n = len(nums)

        nums.sort()
        res = count = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                continue

            elif nums[i] - nums[i - 1] == 1:
                count += 1

            else:
                res = max(count, res)
                count = 1

        return max(count, res)





# 哈希表
# 与 659 差不多
class Solution:
    def longestConsecutive(self, nums):

        res = 0
        num_set = set(nums)

        for num in nums:

            # 如果 num - 1 不在 num_set 的话
            # 就重新开始计数
            if num - 1 not in num_set:
                count = 1
                cur_num = num

                while cur_num + 1 in num_set:
                    cur_num += 1
                    count += 1

                res = max(res, count)

        return res
