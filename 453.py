# 数学题目
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums) if len(nums) != 1 else 0
