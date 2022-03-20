
# O(n)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = res ^ num
        return res




class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            # 如果mid 为偶数，nums[mid]与前面的一样那么单个数字一定出现在前面，
            # 如果mid 为奇数，nums[mid]与后面的一样那么单个数字一定出现在后面

            if mid % 2 == 0 and nums[mid] == nums[mid - 1] or mid % 2 == 1 and nums[mid] == nums[mid + 1]:
                right = mid - 1

            else:
                left = mid + 1

        return nums[left]

