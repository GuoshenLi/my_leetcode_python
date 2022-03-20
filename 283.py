class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # 典型双指针
        j = 0
        for i in range(length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < length:
            nums[j] = 0
            j += 1

# 这个更容易理解！从开头到left - 1储存非零元素，left和right储存0元素，
# left 位置指向第一个非零元素
# 这个是华为面试题
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1




# 拷贝额外数组 违反题目
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        new_num = []
        for item in nums:
            if item != 0:
                new_num.append(item)

        for _ in range(len(nums) - len(new_num)):
            new_num.append(0)

        nums[:] = new_num
