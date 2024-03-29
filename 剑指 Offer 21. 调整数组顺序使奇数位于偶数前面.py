class Solution:
    def exchange(self, nums: List[int]) -> List[int]:

        # 双指针

        left, right = 0, 0
        while right < len(nums):
            if nums[right] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1

        return nums