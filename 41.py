class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)


        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = float('+inf')


        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if 0 <= index <= n - 1:
                if nums[index] > 0:
                    nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1


        return n + 1

# 如果对时间复杂度没有要求
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()

        if nums[0] > 1 or nums[-1] < 1: return 1

        max_ = max(nums)

        for i in range(1, max_ + 1):
            if i not in nums:
                return i

        return max_ + 1