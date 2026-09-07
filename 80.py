# 真牛逼!
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if j < 2 or nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1

        return j

# 感觉这个方法更好想一点
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)

        j, count = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j

# 20260907
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = right = 0
        n = len(nums)
        while right < n:
            count = 1
            while right < n and right + 1 < n and nums[right] == nums[right + 1]:
                count += 1
                right += 1

            if count >= 2: count = 2
            for i in range(min(count, 2)):
                nums[left] = nums[right]
                left += 1
            right += 1

        return left

