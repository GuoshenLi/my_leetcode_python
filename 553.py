# 就是第一个 除以后面几个括号扩起来
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 0: return ""
        if n == 1: return str(nums[0])
        if n == 2: return str(nums[0]) + "/" + str(nums[1])
        res = str(nums[0])
        res += "/(" + str(nums[1])
        for i in range(2, n):
            res += "/" + str(nums[i])
        res += ")"
        return res

