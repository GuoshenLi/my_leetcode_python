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

