from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        p1 = 0
        p2 = len(nums) - 1
        if sorted_nums == nums:
            return 0

        while sorted_nums[p1] == nums[p1]:
            p1 += 1
        while sorted_nums[p2] == nums[p2]:
            p2 -= 1
        return p2 - p1 + 1
