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




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        i = j = 0

        while j < len(nums):

            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1


        return i + 1

# 20260907
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = right = 0
        n = len(nums)

        while right < n:
            while right < n and right + 1 < n and nums[right] == nums[right + 1]:
                right += 1

            nums[left] = nums[right]
            left += 1
            right += 1

        return left