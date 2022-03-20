# 最优解法 找规律
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(left, right):
            while left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k = k % len(nums)

        swap(0, len(nums) - 1)
        swap(0, k - 1)
        swap(k, len(nums) - 1)



# 不会超时 但有额外空间
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        nums_new = [0 for _ in range(length)]
        for i in range(length):
            nums_new[(i + k) % length] = nums[i]
        nums[:] = nums_new

# 会超时
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return nums
        for _ in range(k % length):
            i = nums[0]

            for pointer in range(length - 1, 0, -1):
                nums[(pointer + 1) % length] = nums[pointer]
            nums[1] = i



