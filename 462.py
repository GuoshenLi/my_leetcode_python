# 暴力 通过26/29个用例
class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        unique_val = set(nums)
        res = float('+inf')
        for final_val in unique_val:
            change = 0
            for num in nums:
                if num != final_val:
                    change += abs(final_val - num)
            res = min(res, change)

        return res


# 等价于求中位数

class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        mid = len(nums) // 2
        nums.sort()
        res = 0

        for num in nums:
            res += abs(num - nums[mid])


        return res