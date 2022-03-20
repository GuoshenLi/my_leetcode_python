# 由于是min所以每一个小数都会牺牲掉比它大的数，既然牺牲不可避免，那就牺牲的小一点，排序然后跳跃，跳跳跳
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        return sum(sorted(nums)[::2])


