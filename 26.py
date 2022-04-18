# 双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[j] != nums[i]:
                nums[j + 1] = nums[i]
                j += 1


        return j + 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        j, count = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 1:
                nums[j] = nums[i]
                j += 1

        return j
