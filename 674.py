# 最长递增连续子串
# 和最长递增子序列 不一样
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        count = 1
        res = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        # 注意最后还要弄一个max
        return max(res, count)



