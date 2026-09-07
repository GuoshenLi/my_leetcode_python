# 双指针
# i指向val的位置，j遍历数组看是否是val
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0

        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

            right += 1
        return left